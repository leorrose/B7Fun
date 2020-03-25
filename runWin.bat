@echo off
cmd /k ".\env\Scripts\activate & cd B7FunDjango & start http://localhost:8000/ & python manage.py runserver"