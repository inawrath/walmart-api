FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements/*.txt /code/
RUN pip install -r develop.txt
COPY . /code/
CMD gunicorn --bind 0.0.0.0:$PORT walmart.wsgi
