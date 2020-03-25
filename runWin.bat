@echo off
cmd /k ".\env\Scripts\activate & python manage.py runserver & start http://localhost:8000/ && exit"