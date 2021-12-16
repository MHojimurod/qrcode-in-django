release: python manage.py migrate
web: gunicorn --chdir mysite mysite.wsgi:application --log-file -