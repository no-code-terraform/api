# tfmaker-api (Groupe 4)

GUI in your browser to draw your cloud infrastructure and generate your terraform files.

### Requirements

- [python](https://www.python.org/downloads/) ^3.9
- [MySQL](https://www.mysql.com/fr/) ^8.0

### Tools

- [Django](https://www.djangoproject.com/)

### Set up

- Configure an `.env` file like `.env.sample`
- Run `python -m venv .venv && . .venv/bin/activate`
- Run `python -m pip install -r requirements.txt`

### Get started

- Run `python manage.py migrate`
- Run `python manage.py runserver` || `python -m gunicorn`
- Run `python manage.py createsuperuser`

### Test
- Rum `python manage.py test`

### Run with Docker
- Run `docker build -t tfmaker-api .`
- Run `docker run -p 8000:8000 -it --rm --name tfmaker-api tfmaker-api`
- Run `docker exec -it tfmaker-api sh`
- Run in container `python manage.py createsuperuser`
