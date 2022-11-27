# Achieves

Тестовое задание Achieves

## Requirements
Дополнительные зависимости

* Docker и docker-compose
  * https://docs.docker.com/install/linux/docker-ce/ubuntu/
  * sudo apt install docker-compose
* Postgres


## Deploy
Запуск проекта

* Создать файл .env из файла .env.tmp и настроить переменные окружения
* Запуск БД через докер: `sudo docker-compose up -d`
* Установка зависимостей: `pip install -r requirements.txt`
* Подготовка  
  > $ python manage.py migrate
  > $ python manage.py createsuperuser
* Запуск тестового сервера  
  > $ cd src  
  > $ python manage.py runserver

## Virtual Environment Variables
Все используемые переменные окружения указаны в файле .env.tmp.


## Admin

Доступ к админке по пути `/admin`
