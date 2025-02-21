from fastapi import APIRouter, HTTPException
from models import *
from pydantic import BaseModel, field_validator
from typing import List
from student.models_in import *


student_api = APIRouter()


@student_api.get("/all")
async def getAllStudent():
    students = await Student.all()
    return students


@student_api.get("/filter")
async def getFilterStudent():
    students = await Student.filter(clas_id=2)
    # students=Student.filter(name='rich')
    # students=Student.filter(sno__gt=2001)
    # students=Student.filter(sno__in =[2001,2002])
    # students=Student.filter(sno__range=[1,2001])
    # students=Student.all().values("name","sno")

    return students


@student_api.get("/{student_id}")
async def getOneStudent(student_id: int):
    student = await Student.get(id=student_id)
    return student


@student_api.post("/")
async def addStudent(student_in: StudentIn):
    # method1
    # student=Student(name=student_in.name,pwd=student_in.pwd,sno=student_in.sno,clas_id=student_in.clas_id,courses=student_in.courses)
    # await student.save()
    # method2
    student = await Student.create(name=student_in.name, pwd=student_in.pwd, sno=student_in.sno, clas_id=student_in.clas_id)

    # many to many
    choose_courses = await Course.filter(id__in=student_in.courses)
    await student.courses.add(*choose_courses)

    return student


@student_api.put("/{student_id}")
async def updateStudent(student_id, student_in: StudentIn):
    data = student_in.dict()
    courses = data.pop("courses")
    await Student.filter(id=student_id).update(**data)
    # Student.filter(id=student_id).update(name=student_in.name,sno=student_in.sno)
    # update many to many
    edit_stu = await Student.get(id=student_id)
    choose_courses = await Course.filter(id__in=courses)
    await edit_stu.courses.clear()
    await edit_stu.courses.add(*choose_courses)
    return edit_stu


@student_api.delete("/{student_id}")
async def deleteStudent(student_id):
    deleteCount = await Student.filter(id=student_id).delete()
    if not deleteCount:
        raise HTTPException(status_code=-1, detail=f"student_id {student_id} is not exists")
    return deleteCount
