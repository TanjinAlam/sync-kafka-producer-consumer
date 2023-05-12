# Set python version
ARG BASE_CONTAINER=python:3.9

# Set the base image 
FROM python:3.9

# Make a directory for our consumer
WORKDIR /consumer


# Sets the user name to use when running the image.
# USER root
# RUN apt update && \
#     apt install --no-install-recommends -y build-essential gcc && \
#     apt clean && rm -rf /var/lib/apt/lists/*


# Install dependencies
COPY requirements.txt /consumer/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy current directory to consumer folder
COPY . /consumer/

# Expose the port that the consumerlication runs on
EXPOSE 8001

# Run the consumerlication
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]