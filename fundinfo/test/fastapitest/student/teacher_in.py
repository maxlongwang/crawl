from fastapi import APIRouter
from models import *
from student.models_in import *

teacher_api = APIRouter()


@teacher_api.get("/all")
async def getAllTeacher():
    teacher = await Teacher.all()
    return teacher


@teacher_api.get("/{teacher_id}")
async def getTeacher(teacher_id):
    teacher = await Teacher.get(id=teacher_id)
    return teacher


@teacher_api.delete("/{teacher_id}")
async def deleteTeacher(teacher_id):
    row = await Teacher.get(id=teacher_id).delete()
    return row


@teacher_api.put("/{teacher_id}")
async def updateTeacher(teacher_id, teacher_in: TeacherIn):
    data = teacher_in.model_dump()
    row = await Teacher.filter(id=teacher_id).update(**data)
    return row


@teacher_api.post("/add")
async def insertTeacher(teacher_in: TeacherIn):
    teacher = await Teacher.create(name=teacher_in.name, pwd=teacher_in.pwd, tno=teacher_in.tno)
    return teacher
