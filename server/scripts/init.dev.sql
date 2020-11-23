CREATE DATABASE placesremember;
CREATE USER manager WITH PASSWORD 'password';
ALTER ROLE manager SET client_encoding TO 'utf8';
ALTER ROLE manager SET default_transaction_isolation TO 'read committed';
ALTER ROLE manager SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE placesremember TO manager;
ALTER USER manager CREATEDB;
