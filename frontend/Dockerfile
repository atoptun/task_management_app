# Використовуємо базовий образ node
FROM node:22

# Встановлюємо робочу директорію
WORKDIR /app

# Копіюємо package.json і package-lock.json для встановлення залежностей
COPY package*.json ./

# Встановлюємо залежності
RUN npm install

# Копіюємо решту файлів проєкту
COPY . .

# Вказуємо порт 3000
EXPOSE 3000

# Запускаємо додаток
CMD ["npm", "start"]
