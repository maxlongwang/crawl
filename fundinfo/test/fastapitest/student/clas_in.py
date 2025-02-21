from fastapi import APIRouter
from models import *
from student.models_in import *

clas_api = APIRouter()


@clas_api.get("/all")
async def getAllClas():
    clas = await Clas.all()
    return clas


@clas_api.get("/{clas_id}")
async def getClas(clas_id):
    clas = await Clas.get(id=clas_id)
    return clas


@clas_api.delete("/{clas_id}")
async def deleteClas(clas_id):
    row = await Clas.get(id=clas_id).delete()
    return row


@clas_api.put("/{clas_id}")
async def updateClas(clas_id, clas_in: ClasIn):
    data = clas_in.model_dump()
    row = await Clas.filter(id=clas_id).update(**data)
    return row


@clas_api.post("/add")
async def insertClas(clas_in: ClasIn):
    clas = await Clas.create(name=clas_in.name)
    return clas
