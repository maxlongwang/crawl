from fastapi import APIRouter
from models import *
from student.models_in import *



course_api = APIRouter()


@course_api.get("/allcousre")
async def getAllCourse():
    course = await Course.all()
    return course


@course_api.get("/{course_id}")
async def getCourse(course_id):
    course = await Course.get(id=course_id)
    return course


@course_api.delete("/{course_id}")
async def deleteCourse(course_id):
    course = await Course.get(id=course_id).delete()
    return course


@course_api.put("/{course_id}")
async def putCourse(course_id, course_in:CourseIn):
    data = course_in.dict()
    course = await Course.filter(id=course_id).update(**data)
    return course


@course_api.post("/addCourse")
async def postCourse(course_in:CourseIn):
    course = await Course.create(name=course_in.name, teacher_id=course_in.teacher_id)
    return course

