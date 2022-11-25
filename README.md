# About
Проект разработан в рамках знакомства с FastAPI.
Тематика - опросы

#### API приложения предусматривает следующий функционал:

- Авторизация, регистрация
- CRUD для опросов
- Голосование в опросе

#### Приложение работает с трёмя таблицами:

- Опросы - polls
- Выборы - choices
- Голоса - votes

#### Также используются технологии:

- SQLAlchemy
- Pydantic
- Docker

# How to run
### Склонировать репозиторий
```
git clone https://github.com/Potagashev/polls.git
```
### Запустить
```
docker-compose up
```
### Создать таблицы
```
docker-compose run web python create_tables.py
```
