# Используем базовый образ Python
FROM python:3.9-slim-buster

# Устанавливаем зависимости проекта
RUN apt-get update && apt-get install -y \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Копируем проект в контейнер
COPY . /app

# Устанавливаем переменную окружения для Django
ENV DJANGO_SETTINGS_MODULE=jutsu_sohr.settings.production

# Запускаем приложение
CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]