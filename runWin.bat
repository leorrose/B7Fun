@echo off
cmd /k ".\env\Scripts\activate & cd B7FunDjango & python manage.py runserver & start http://localhost:8000/ "