# Money_Manager - Менеджер персональных финансов

Данный проект представляет собой учебный проект, созданный с целью изучения фреймворка Flask.

## Описание проекта

LP_PFM - это веб-приложение, которое предназначено для управления персональными финансами пользователей. Оно позволяет регистрироваться, создавать счета, отслеживать транзакции и анализировать финансовые данные.

## Технологии и инструменты

- Python 3.10
- Flask
- SQLAlchemy 2.0
- SQLite/Postgresql
- HTML/CSS
- Bootstrap

## Установка Poetry

Если вы используете Windows, выполните следующую команду в PowerShell:
```power shell
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Other os
[Instruction](https://python-poetry.org/docs/#installation)

## Установка и запуск проекта

1. Клонируйте репозиторий и перейдите в папку проекта:

`git clone git@github.com:babanlive/Money_Manager.git && cd Money_Manager`

2. Установка проекта:

```shell
poetry install
```

3. Запуск сервера FLASK

```shell
poetry run flask run --debug
```

## Использование

После запуска проекта, вы можете открыть веб-страницу по адресу:\
[http://localhost:5000/](http://localhost:5000/)

## Регистрация и вход в систему
- Для входа в систему вы можете зарегистрироваться - нажмите кнопку "Регистрация" и заполните форму.