DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_user WHERE usename = 'limited_user'
   ) THEN
      CREATE USER limited_user WITH PASSWORD 'limited_password';
   END IF;
END
$do$;

GRANT CONNECT ON DATABASE taskdb TO limited_user;

GRANT USAGE ON SCHEMA public TO limited_user;

GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO limited_user;

ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT, INSERT, UPDATE, DELETE ON TABLES TO limited_user;
