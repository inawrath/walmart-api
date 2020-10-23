import mongoengine

from mongoengine import connect

from .settings import *  # NoQA

mongoengine.connection.disconnect()

connect('testdb', host='mongomock://localhost')
