FROM python:alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем обновления и необходимые модули
RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

# Обновление pip python
RUN pip install --upgrade pip
WORKDIR /app
# Установка пакетов для проекта
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN ls
COPY . .

EXPOSE 8000
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
