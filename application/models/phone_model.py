from tortoise.models import Model
from tortoise.fields import CharField, IntField


class Phone(Model):
    id = IntField(pk=True)
    phone = CharField(max_length=15)

