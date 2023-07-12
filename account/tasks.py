import os

from celery import shared_task
from django.core.mail import send_mail
from decouple import config

HOST = os.getenv('HOST', default='127.0.0.1')


@shared_task
def send_confirmation_email(user_email, code):
    link = f'http://{HOST}/accounts/activate/{code}/'
    msg = f'Здраствуйте, актривируйте ваш аккаунт!\nЧто бы активировать ваш аккаунт нужно перейти по ссылки ниже:\n{link}\nСсылка работает один раз!'

    send_mail(
        subject='Активация аккаунта <no-reply>',
        message=msg,
        from_email=config('EMAIL_USER'),
        recipient_list=[user_email],
    )
