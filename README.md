# youtube-python-djano-tutorial
 
Python Tutorial for [Django Developers](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)

Extra courses in [LearnDjango](https://learndjango.com/courses/)

## Installation:
```bash
pip install django
```

## Check Django Version:
```bash
python -m django --version
```

## Django Admin:
```bash
django-admin
```

## Create Django Project:
```bash
django-admin startproject django_project
```

## Run Django Server:
```bash
python django_project/manage.py runserver
```

## Create Django App:
```bash
python django_project/manage.py startapp blog 
python manage.py startapp blog // if you are in the project directory
```

## Create Super User:
```bash
python manage.py createsuperuser
python manage.py createsuperuser --username admin --email
```

- If you are not in the project directory:

```bash
python django_project/manage.py createsuperuser 
python django_project/manage.py createsuperuser --username admin --email 
```

## Migrate Database:
```bash
python manage.py makemigrations
```

## Apply Migrations:
```bash
python manage.py migrate
```

username: admin
email: admin@gmail.com
password: admin

ORM: Object Relational Mapping

## SQL Migration:
```bash
python manage.py sqlmigrate blog 0001
```

## Django Shell:
```bash
python manage.py shell
```

## Quering Data:
```
python manage.py shell

from blog.models import Post
from django.contrib.auth.models import User

User.objects.all() // Get all users

User.objects.first() // Get first user

User.objects.filter(username='admin') // Get all users with username admin

User.objects.filter(username='admin').first() // Get first user with username admin

User.objects.filter(username='admin').first().id // Get id of first user with username admin

User.objects.filter(username='admin').first().pk // Get primary key of first user with username admin

User.objects.filter(username='admin').first().email // Get email of first user with username admin

User.objects.get(id=1) // Get user with id 1
```

## Cmds:
```bash
from blog.models import User
from django.contrib.auth.models import User
from blog.models import Post

```


Every time you make changes to the models, you need to run the following commands:

```bash
python django_project/manage.py makemigrations
python django_project/manage.py migrate
```