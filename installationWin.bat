@echo off
cmd /k "python -m pip install --upgrade pip & pip install virtualenv & virtualenv env & .\env\Scripts\activate & pip install --no-cache-dir -r requirements.txt && exit"