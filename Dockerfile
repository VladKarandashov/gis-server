# Используем официальный образ Python в качестве базового
FROM python:3.9-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Устанавливаем зависимости
RUN pip install psycopg2-binary

# Копируем ваш скрипт в контейнер
COPY main.py .

EXPOSE 80

# Команда для запуска вашего приложения
CMD ["python", "main.py"]
