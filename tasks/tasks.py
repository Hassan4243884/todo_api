from todo_list.celery_app import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task
from datetime import timedelta


@shared_task
def send_task_reminders():
    now = timezone.now()
    upcoming_tasks = Task.objects.filter(
        deadline__lt=now + timedelta(hours=24), completed=False
    )

    for task in upcoming_tasks:
        send_mail(
            "Task Reminder",
            f'Reminder: Your task "{task.title}" is due soon!',
            "from@example.com",
            [task.user.email],
            fail_silently=False,
        )
