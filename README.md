# tree-menu-django

--- 

### Описание
Приложение Django, в котором с помощью tamplate tag 
реализовано древовидное меню, редактируемое в админке Django. Меню по 
названию можно отрисовать на любой странице Приложения, 
используя следующие теги:
```
{% load draw_menu %}
{% draw_menu 'main_menu' %}
```

### Технологии
* Python
* Django

### Запуск проекта
Для Windows:

```shell
git clone git@github.com:elityaev/tree-menu-django.git
cd tree-menu-django
python -m venv venv
venv/Scripts/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```
Для Linux:

```shell
git clone git@github.com:elityaev/tree-menu-django.git
cd tree-menu-django
python3 -m venv venv
source venv/bin/activat
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
```

Для корректной работы приложения необходимо:
 * создать суперпользователя
```shell
python manage.py createsuperuser
```
 * создать меню и его элементы через административную панель.

Запустить сервер разработки
```shell
python manage.py runserver
```
