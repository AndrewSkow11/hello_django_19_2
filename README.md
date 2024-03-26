**Проект домашних работ по Django**

*Развёртывание проекта*

- Установить зависимости из файла requirements.txt (корневая папка проекта)

- Создать базу данных с именем db_for_django_project: 
```
% psql -U postgres
postgres=# create database db_for_django_project;
CREATE DATABASE
```
- Создать файл .env, в котором задать значение переменных:
    POSTGRES_PASSWORD (пароль базы данных)
    EMAIL_HOST=smtp.yandex.ru (пример, можно использовать другой)
    EMAIL_HOST_USER=example@yandex.ru
    EMAIL_HOST_PASSWORD=your_application_password


- Создать суперпользователя можно командой, по умолчанию:
- email: admin@admin.ru,
- password: 1234
```commandline
python3 manage.py create_superuser
```

- Рекомендуется также обновить сертификаты
```commandline
pip install --upgrade certifi
```

- в случае неработоспособности с пустой базой данных
```
./manage.py migrate sites
./manage.py migrate
```

Дополнения после работы 23_2

```commandline
brew install redis
pip install redis

redis-server
```
