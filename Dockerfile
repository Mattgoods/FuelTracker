# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /code
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libaio1 \
    make \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Download and install Oracle Instant Client
RUN wget -O instantclient-basic-linux.x64-21.13.0.0.0dbru.zip https://download.oracle.com/otn_software/linux/instantclient/2113000/instantclient-basic-linux.x64-21.13.0.0.0dbru.zip \
    && unzip instantclient-basic-linux.x64-21.13.0.0.0dbru.zip -d /opt/oracle \
    && sh -c "echo /opt/oracle/instantclient > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig \
    && ls -l /opt/oracle/instantclient

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_21_13:$LD_LIBRARY_PATH
ENV PATH=/opt/oracle/instantclient_21_13:$PATH

# Copy the current directory contents into the container at /code
COPY . /code

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run run.py when the container launches
CMD ["python", "run.py"]
