@echo off
cd ..
cmd /c ".\env\Scripts\activate & cd B7FunDjango & start http://localhost:8000/ & python manage.py runserver"
