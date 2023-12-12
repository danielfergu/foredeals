DROP SCHEMA IF EXISTS foredeals CASCADE;

drop database if exists foredeals;
drop user if exists foredeals;

create user foredeals with encrypted password 'foredeals';
create database foredeals;
grant all privileges on database foredeals to foredeals;
\c foredeals
grant create on schema public to foredeals;

