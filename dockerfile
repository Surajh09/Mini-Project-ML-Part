# Use an official Python runtime as a parent image
FROM python:3.6.8

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /

# Install dependencies
RUN apt-get update && apt-get install -y --fix-missing \
  build-essential \
  cmake \
  gfortran \
  libatlas-base-dev \
  libblas-dev \
  liblapack-dev \
  libsvm-dev \
  libopenblas-dev \
  python3-dev \
  && apt-get clean && rm -rf /tmp/* /var/tmp/*
COPY requirements.txt /
RUN pip install -r requirements.txt

# Copy project
COPY . /SMS/

# Run gunicorn
CMD gunicorn Attendence_System.wsgi:application --bind 0.0.0.0:$PORT