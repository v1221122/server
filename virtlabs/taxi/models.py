from django.db import models

# Create your models here.
from peewee import *

database = MySQLDatabase('alex', **{'user': 'root'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Workers(BaseModel):
    car = CharField()
    name = CharField()
    work = IntegerField(null=True)

    class Meta:
        db_table = 'workers'

