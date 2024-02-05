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

- Для работы с административной панелью Django необходимо создать суперпользователя (типичный сценарий представлен ниже):
```commandline
% python3 manage.py createsuperuser
Username : admin
Email address:  
Password: 
Password (again): 
Superuser created successfully.
```

