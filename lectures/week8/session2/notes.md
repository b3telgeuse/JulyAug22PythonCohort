Resources and hackathon links

https://hackmd.io/o0xnYRLYRx2yMr9bmY2Lxw

Java notes
https://hackmd.io/UDcgU13gROax7Wom35DvHQ

React notes
https://www.notion.so/honeybee24/Some-extra-links-7c3ad2647eda45a48989004a1c27baca


Melissa's LinkedIn
https://www.linkedin.com/in/melissa-longenberger/

## Create Django environment
python -m venv jokesEnv

## to Activate
source jokesEnv/bin/activate (mac)
source jokesEnv/Scripts/activate (windows)

## pip install 
django
bcrypt

## Create django project
django-admin startproject jokes

## create app
python manage.py startapp jokesApp

## Run server
python manage.py runserver

## create super user (for django admin)
python manage.py createsuperuser - then follow prompts

## After models are build
python manage.py makemigrations
python manage.oy migrate

## on admin.py (for django admin)
admin.site.register(ClassName)