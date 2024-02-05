**Проект домашних работ по Django**

*Развёртывание проекта*

- Установить зависимости из файла requirements.txt (корневая папка проекта)

- Создать базу данных с именем db_for_django_project: 
```
% psql -U postgres
postgres=# create database db_for_django_project;
CREATE DATABASE
```
- Создать файл .env, в котором задать значение переменной POSTGRES_PASSWORD (пароль базы данных)


