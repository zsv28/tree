[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&width=435&lines=Tree_menu)](https://git.io/typing-svg)

### Проект древовидного меню Django

Это проект Django, который реализует древовидное меню со следующими возможностями:
- Древовидная структура меню, хранящаяся в базе данных.
- Редактирование через админку Django.
- Поддержка нескольких меню на одной странице.
- Рендеринг меню с помощью пользовательского тега шаблона.
- 
### Технологии
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)


- Python 3.10
- Django 5.1

#### Локальный запуск проекта

- Склонировать репозиторий:

```bash
   git clone git@github.com:zsv28/tree.git
```


В папке с проектом создать и активировать виртуальное окружение:

- Команда для установки виртуального окружения на Mac или Linux:

```bash
   python3 -m venv env
   source env/bin/activate
```

- Команда для Windows:

```bash
   python -m venv venv
   source venv/Scripts/activate
```

- Установить зависимости из файла requirements.txt:

```bash
   pip install -r requirements.txt
```

- Сделать миграции:

```bash
    python manage.py migrate
```

- Загрузить тестовые данные:

```bash
    python manage.py loaddata tree_menu/fixtures/test_menu.json
```

- Создайте суперпользователя для админки:

```bash
    python manage.py createsuperuser
```


- Запустить локальный сервер:

```bash
   python main.py runserver
```


#### Откройте проект в браузере:

Перейдите по адресу http://127.0.0.1:8000/ для просмотра главной страницы или /admin для входа в админку.
