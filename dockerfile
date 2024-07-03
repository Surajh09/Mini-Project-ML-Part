# Use a slim Python image for a smaller footprint
FROM python:3.11.7-slim

# Install dependencies
RUN apt-get update && apt-get install -y python3-pip

# Create a working directory
WORKDIR /app

# Install face_recognition and OpenCV (commonly used with face_recognition)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy your application code (replace . with your code directory)
COPY . .

# Expose a port (optional, replace 8000 with your desired port)
EXPOSE 8000

# Entrypoint (replace with your application's startup command)
CMD [ "python", "manage.py", "runserver" ]
