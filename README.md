# API YaMDb
Проект YaMDb собирает отзывы пользователей на произведения.
Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку.


### Технологии:
Python 3.7, Django 2.2.16, DRF, JWT + Djoser

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:

```
https://github.com/BiftAL/api_yamdb.git
```

```
cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

Для Windows:
```
source venv/Scripts/activate
```

Для Linux и MacOS:
```
source venv/bin/activate
```

Обновить менеджер пакетов
```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Перейти в каталог с файлом manage.py
```
cd api_yamdb/
```

Переименовать и отредактировать в корне проекта файл env.example в .env
```
mv env.example api_yamdb/.env
nano api_yamdb/.env
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов эндпоинтов:

##### Для любых пользователей

```
GET api/v1/categories/ - получить список всех категорий
GET api/v1/genres/ - получить список всех жанров

GET api/v1/titles/ - получить список всех произведений
GET api/v1/titles/{titles_id}/ - получение конкретного произведения

GET api/v1/titles/{title_id}/reviews/ - получить список всех отзывов поизведения
GET api/v1/titles/{title_id}/reviews/{review_id}/ - получение конкретного откзыва к произведению

```
##### Для авторизованных пользователей

Создание публикации:
```
POST /api/v1/categories/
```
Поля запроса:

```
body: { "name": "string", "slug": "string" }
```

Детальная информация по всем эндпоинтам есть в документации. При запущенном проекте документация доступна по ссылке:

```
http://127.0.0.1:8000/redoc/
```

Для запуска тестов:
```
cd ..
pytest
```
