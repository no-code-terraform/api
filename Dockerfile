FROM python:3.10.7-bullseye

WORKDIR /usr/src/app

COPY .env ./
COPY requirements.txt ./

RUN python -m pip install -r requirements.txt

COPY . .

RUN python manage.py migrate
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]