# Проект СПИСОК РЕГИОНОВ И ГОРОДОВ

Приложение реализовано с использование фреймворка Flask, библиотеки SQLAlchemy. В качестве базы данных использован PostgreSQL.

## Суть проекта
Разработать REST-API для управления списком регионов и городов, которые в них входят.
Необходимо реализовать выборку регионов, выборку городов по региону, CRUD для городов и регионов.
Для неавторизованного пользователя должны быть доступны только выборки данных.
Управление записями пользователей через REST-API не предполагается

## Оговорки и допущения
В системе должена быть установлена СУБД PostgreSQL.
В СУБД должна быть создана пустая база данных с произвольным наименованием.
Аутентификация пользователей выполняется непосредственной проверкой наличия в http-запросах (в необходимых случаях) заголовков "username" и "password",
и сравнения этих данных с имеющимися в базе.
Пароли хранятся в БД не в открытом виде, а в виде хеша.

## Разворачивание проекта
1. Создать директорию, в которую будет помещен каталог с проектом
2. Выполнить команду `git clone https://github.com/stanislav-akolzin/locations.git`
3. Зайти в выбранный каталог и выполнить команду `python<veresion> -m venv env` для создания виртуального окружения под именем 'env'
4. Выполнить команду `. env/bin/activate` для активации виртуального окружения
5. Выполнить команду `pip install -r requirements.txt` для установки всех зависимостей для проекта из файла requirements.txt
6. Необходимо заполнить в config.py НаименованиеБД, ИмяПользователяБД и ПарольПользователяБД
7. Запустить скрипт db_initialization_and_filling_script.py для создания в базе данных 2-х пользователей (John и Bill с паролями 'john_password' и 'bill_password'
соответственно), 10 регионов и по несколько городов в этих регионах.
8. Далее можно тестировать проект, запустив run.py

## Разворачивание проекта из Docker
1. Перейти в директорию, в которую будет добавлен каталог с ихсодниками проекта
2. Выполнить команду `git clone https://github.com/stanislav-akolzin/locations.git`
3. Перейти в созданный каталог проекта `locations`
4. Создать новую базу данных в локально установленном Postgresql с произвольным именем `<basename>`
5. В файле `config.py` заполнить наименование базы данных (`<basename>`), а также ИмяПользователяБД и ПарольПользователяБД
6. Создать образ из Dockerfile - `docker build -t <image_name> .`
7. Запустить контейнер приложения из образа - `docker run --rm --name <container_name> -p 8000:8000 --network=host <image_name>`
8. Выполнить команду создания в базе данных 2-х пользователей (John и Bill с паролями 'john_password' и 'bill_password'
соответственно), 10 регионов и по несколько городов в этих регионах - `docker exec <container_name> python db_initialization_and_filling_script.py`
9. Можно тестировать проект

## Описание API

### Получение списка регионов
Вывод списка всех имеющихся в БД регионов с их идентификаторами

`GET /api/regions`

Тело ответа
```
{
  "regions": [
        {
            "id": <region id>,
            "name": "<region name"
        },
        {
            "id": <region id>,
            "name": "<region name>"
        }
    ]
}
```

### Получение списка городов региона
Выводит список всех городов переданного в параметре региона

`GET api/cities/<region_id>`

Параметры:
`region_id` - идентификатор региона

Тело ответа
```
{
    "cities": [
        {
            "id": <city id>,
            "name": "<city name>"
        },
        {
            "id": <city id>,
            "name": "<city name>"
        }
    ]
}
```

### Добавление региона в БД
Добавляет в БД переданный в теле запроса регион. Для выполнения требуется авторизация

`POST api/add_region`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса
```
{
    "name": "<region name>"
}
```

Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "Region already exists"
}
```
```
{
    "error": "No region name given"
}
```

### Добавление города в список городов региона
Добавляет в БД переданный в теле запроса город в переданный в теле запроса регион. Для выполнения требуется авторизация

`POST api/add_city`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса 
```
{
    "region_id": <region id>,
    "city_name": "<city name>"
}
```

Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "No region id or city name given"
}
```
```
{
    "error": "Wrong region id"
}
```
```
{
    "error": "City in that region already exists"
}
```

### Изменение региона
Меняет наименование переданного в теле запроса региона. Для выполнения требуется авторизация

`PUT api/change_region`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса
```
{
    "region_id": <region id>,
    "region_name": "<region name>"
}
```
  
Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "No city id given"
}
```
```
{
    "error": "Wrong region id"
}
```
  
### Изменение города
Меняет наименование или регион переданного в теле запроса города. Для выполнения требуется авторизация

`PUT api/change_city`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса
```
{
    "city_name": "<city name>",
    "city_id": <city id>,
    "region_id": <region id>
}
```

`city_name` и `region_id` - опциональны

Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "No city id given"
}
```
```
{
    "error": "Wrong city id"
}
```
```
{
    "error": "Wrong region id"
}
```

### Удаление региона
Удаляет переданный в теле запроса регион и все относящиеся к нему города из БД. Для выполнения требуется авторизация

`DELETE api/delete_region`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса
```
{
    "region_id": <region id>
}
```

Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "Wrong region id"
}
```
```
{
    "error": "No region id given"
}
```

### Удаление города
Удаляет переданный в теле запроса город из БД. Для выполнения требуется авторизация

`DELETE api/delete_city`

Заголовки:

`username` - имя пользователя

`password` - пароль пользователя

Тело запроса
```
{
    "city_id": <city_id>
}
```

Примеры тела ответа
```
{
    "status": "success"
}
```
```
{
    "error": "Wrong city id"
}
```
```
{
    "error": "No city id given"
}
```
