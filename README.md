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

## Описание API

### Получение списка регионов
Вывод списка всех имеющихся в БД регионов с их идентификаторами

`GET /api/regions`

Тело ответа

```{
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
}```
