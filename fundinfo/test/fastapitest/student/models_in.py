from pydantic import BaseModel, field_validator
from typing import List


class StudentIn(BaseModel):
    name: str
    pwd: str
    sno: int
    clas_id: int
    courses: List[int] = []

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must bu alpha'
        return value

    @field_validator("sno")
    def sno_validator(cls, value):
        assert value > 1000 and value < 5000, 'sno between 1000 and 5000'
        return value


class TeacherIn(BaseModel):
    name: str
    pwd: str
    tno: int


class CourseIn(BaseModel):
    name: str
    teacher_id: int
    
class ClasIn(BaseModel):
    name:str
