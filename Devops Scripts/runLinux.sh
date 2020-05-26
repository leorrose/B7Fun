#!/bin/sh
sudo apt-get install xdg-utils --fix-missing
cd ..
. env/bin/activate
cd B7FunDjango/
xdg-open http://localhost:8000/
python3 manage.py runserver

