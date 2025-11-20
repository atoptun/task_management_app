#!/bin/bash
set -e

# Створення SQL-скрипта на льоту з використанням змінних оточення
# Зверніть увагу, що змінні Bash (наприклад, $POSTGRES_DB) доступні тут,
# оскільки вони передаються у Docker-контейнер з docker-compose.
# Змінні для limited_user потрібно буде додати в .env та compose.yaml

SQL=$(cat <<EOF
-- Створення користувача з використанням змінних оточення
DO
\$do\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_user WHERE usename = '$LIMITED_USER'
   ) THEN
      CREATE USER $LIMITED_USER WITH PASSWORD '$LIMITED_PASSWORD';
   END IF;
END
\$do\$;

-- Надання прав доступу
GRANT CONNECT ON DATABASE $POSTGRES_DB TO $LIMITED_USER;
GRANT USAGE ON SCHEMA public TO $LIMITED_USER;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO $LIMITED_USER;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO $LIMITED_USER;

EOF
)

# Виконання SQL-скрипта, коли база даних taskdb буде готова.
# Використовуємо psql, підключившись як суперкористувач.
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    $SQL
EOSQL

echo "Limited user '$LIMITED_USER' created and granted necessary privileges on database '$POSTGRES_DB'."
