from tortoise import fields
from tortoise.models import Model


class Student(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=322, description='username')
    pwd = fields.CharField(max_length=322, description='password')
    sno = fields.IntField(description="xuhao")
    clas = fields.ForeignKeyField("models.Clas", related_name='student')
    courses = fields.ManyToManyField("models.Course", related_name='student')


class Clas(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=322, description='classname')


class Course(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=322, description='coursename')
    teacher = fields.ForeignKeyField("models.Teacher")
    # addr=fields.CharField(max_length=322,description='address',default="")


class Teacher(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=322, description='teachname')
    pwd = fields.CharField(max_length=322, description='password')
    tno = fields.IntField(description='teach no')
