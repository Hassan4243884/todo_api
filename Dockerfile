# Dockerfile
# Use official Python runtime as a base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /usr/src/app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port 8000
EXPOSE 8000

# Run the application
CMD ["gunicorn", "todo_list.wsgi:application", "--bind", "0.0.0.0:8000"]
