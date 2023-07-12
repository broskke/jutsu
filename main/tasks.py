from account.send_mail import send_confirmation_email
from .celery import app


@app.task
def send_confirmation_mail_task(user, code):
    send_confirmation_email(user, code)
