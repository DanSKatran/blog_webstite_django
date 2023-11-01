# django_sprint4

cd blog_website/

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

python manage.py runserver


Usage:
- Create a superuser
- superuser will post videos, images, and text

Built With:
- Django
- Python

to add new language:
django-admin makemessages -l en -e html
django-admin compilemessages