# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /code
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libaio1 \
    make \
    && rm -rf /var/lib/apt/lists/*

# Install Oracle instant client (adjust as necessary for your setup)
# ADD instantclient-basic-linux.x64-19.3.0.0.0dbru.zip /opt/oracle
# RUN unzip /opt/oracle/instantclient-basic-linux.x64-19.3.0.0.0dbru.zip -d /opt/oracle \
#     && sh -c "echo /opt/oracle/instantclient_19_3 > /etc/ld.so.conf.d/oracle-instantclient.conf" \
#     && ldconfig

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
