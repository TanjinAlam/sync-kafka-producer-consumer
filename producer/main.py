import time

from gateway.kafka import Kafka
from utils.kafka import get_kafka_producer
from routers import publisher
from decouple import config

from dotenv import load_dotenv

from fastapi import Depends, FastAPI, Request

load_dotenv()


app = FastAPI(title='Kafka Producer API')
kafka_server = Kafka(
    topic=config("KAFKA_TOPIC_NAME"),
    port=config("KAFKA_PORT"),
    servers=config("KAFKA_SERVER") 
)


@app.on_event("startup")
async def startup_event():
    await kafka_server.aioproducer.start()


@app.on_event("shutdown")
async def shutdown_event():
    await kafka_server.aioproducer.stop()


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get('/')
def get_root():
    return {'message': 'Producer API is running...'}


app.include_router(
    publisher.router,
    prefix="/producer",
    tags=["producer"],
    dependencies=[Depends(get_kafka_producer)],
)
