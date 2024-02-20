# django_sprint4

cd blog_website_django/

python -m venv venv

source venv/bin/activate

pip install -r requirements.txt

cd blog_website/

python manage.py runserver ip:port


Usage:
- Create a superuser
- superuser will post videos, images, and text

Built With:
- Django
- Python

to add new language:
django-admin makemessages -l en -e html

django-admin compilemessages


Useful commands for setting up the project on server:
sudo systemctl restart gunicorn
sudo systemctl restart nginx
sudo systemctl reload nginx
