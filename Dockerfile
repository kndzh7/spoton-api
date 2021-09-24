FROM python:3.7

WORKDIR /app
ADD ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ADD . /app
CMD python manage.py migrate && gunicorn -b 0.0.0.0:8000 --log-level info --reload -w 9 spoton.wsgi:application
