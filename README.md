# socks_shop

## Description
This is a small project that is the final part of SDA course "Python beginner". It is intended to be a basic e-commerce website built using Django. For simplicity it uses a sqlite database. On the front end we use some bootstrap 4 and MDB. Some parts of the code are based on https://github.com/justdjango/django-ecommerce.

## Installation
+ Run `pip install -r .\requirements.txt`. The file is included in the repository. This will install the required packeges and dependencies.
+ While in the folder containing the file `manage.py`, run `python manage.py makemigrations` and `python manage.py migrate`. This creates the local sqlite database file on your machine.
+ Run `python manage.py runserver` if you want to start the project for development. You should see
```python
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
September 20, 2021 - 20:37:41
Django version 3.2.6, using settings 'skiety.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```
Go to `http://127.0.0.1:8000/` in your browser to see the website.

## What to expect in the future (status: IX 2021)
+ Expand the website's functionalities
+ Dockerize the project
