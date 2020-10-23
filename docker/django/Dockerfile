FROM python:3.9.0
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY ./requirements/*.txt /code/
RUN pip install -r develop.txt
COPY . /code/
