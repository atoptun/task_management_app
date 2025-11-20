# Використовуємо базовий образ python
FROM python:3.12

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо requirements.txt для встановлення залежностей
COPY requirements.txt ./

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо інші файли проєкту
COPY . .

# Задаємо порт 5000
EXPOSE 5000

# Запускаємо додаток
CMD ["python", "run.py"]
