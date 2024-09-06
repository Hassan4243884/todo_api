# Django Todo List API

This project is a Todo List API built using Django, incorporating Celery for background task processing, with Docker for containerization. Users can manage their tasks and categories, and receive email reminders for upcoming deadlines.

## Features

- **User Authentication**: Token-based authentication (using Django REST framework).
- **Task Management**: Add, retrieve, update, delete tasks with title, description, deadline, priority, and completion status.
- **Category Management**: Add and manage task categories. Filter tasks by category.
- **Email Reminders**: Celery is used to send email reminders 24 hours before task deadlines.
- **Dockerized**: Containerized using Docker for easy deployment.
- **API Documentation**: A Postman collection is included for testing the API endpoints.

## Prerequisites

Ensure you have the following installed:

- Docker: [Install Docker](https://docs.docker.com/get-docker/)
- Docker Compose: [Install Docker Compose](https://docs.docker.com/compose/install/)
- Redis: Used as the broker for Celery.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Hassan4243884/todo_api.git
   cd todo_api
   ```

2. Set up environment variables:
   Create a `.env` file in the project root with the following:

   ```bash
   CELERY_BROKER_URL=redis://redis:6379/0
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations:

   ```bash
   python manage.py migrate
   ```

## Running the Application Locally

### Make sure to edit django settings for email configurations
   

2. Start the development server:

   ```bash
   python manage.py runserver
   ```

3. Start Celery worker:

   ```bash
   celery -A todo_list worker --loglevel=info
   ```

4. Start Celery Beat for scheduled tasks:
   ```bash
   celery -A todo_list beat --loglevel=info
   ```

The application will be available at `http://127.0.0.1:8000/`.

## Running the Application with Docker

1. Build and start the Docker containers:

   ```bash
   docker-compose up --build
   ```

2. Run database migrations:

   ```bash
   docker-compose exec web python manage.py migrate
   ```

The application will be available at `http://localhost:8000/`.

## Celery Setup

- **Worker**: Celery worker runs background tasks for sending email reminders.
- **Beat**: Celery Beat is used for scheduling periodic tasks like checking for upcoming task deadlines.

Both services are automatically started with Docker using the following commands:

- Celery Worker: `celery -A todo_list worker --loglevel=info`
- Celery Beat: `celery -A todo_list beat --loglevel=info`

Logs can be viewed using:

```bash
docker-compose logs celery
docker-compose logs celery-beat
```

## Postman API Documentation

The Postman collection for the API is included in the project. You can use it to test the API endpoints.

To import the collection into Postman:

- Open Postman.
- Click Import.
- Select the TodoApp.json file in the root folder.
- You can now interact with the API endpoints in Postman

### API Documentation

- https://documenter.getpostman.com/view/27232575/2sAXjRUott
