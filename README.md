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


## API

### Feed  
Лента событий  

GET /api/feed/

Параметры:
q `<string>` - поиск событий (по title)
limit `<integer>` - количество элементов
offset `<integer>` - сдвиг элементов
user_id `<integer>` - ID пользователя
content_type `<integer>` - тип события в ленте

Пример запроса
```
GET /api/feed/?limit=10&offset=5&user_id=1&content_type=13&q=test
```
