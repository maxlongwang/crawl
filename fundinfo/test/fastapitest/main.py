from fastapi import FastAPI,  Response, Request
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import fastapi_cdn_host

from app01.urls import user
from app02.urls import shop
from student.student_in import student_api
from student.course_in import course_api
from student.teacher_in import teacher_api
from student.clas_in import clas_api

from app04.test import test
import time


from tortoise.contrib.fastapi import register_tortoise

from setting import TORTOISE_ORM


app = FastAPI()
fastapi_cdn_host.patch_docs(app)
app.include_router(shop, prefix="/shop", tags=["shop"])
app.include_router(user, prefix="/user", tags=["user"])
app.include_router(student_api, prefix="/student", tags=["student"])
app.include_router(course_api, prefix="/course", tags=["course"])
app.include_router(teacher_api, prefix="/teacher", tags=["teacher"])
app.include_router(clas_api, prefix="/class", tags=["class"])
app.include_router(test, prefix="/test", tags=["test"])


register_tortoise(app=app, config=TORTOISE_ORM)

# app.add_middleware(CORSMiddleware, allow_origins="*"
#                    #    ,allow_credentials=True
#                    #    ,allow_methods=["GET"]
#                    #    ,allow_headers=["*"]
#                    )

# @app.middleware("http")
# async def MyCORSMiddleware(request:Request,call_next):
#     response=await call_next(request)
#     response.headers["Access-Control-Allow-Origin"]="*"

#     return response


# @app.middleware("http")
# async def m2(request: Request, call_next):
#     print("m2 request")
#     response = await call_next(request)

#     # response code
#     response.headers["author"] = "max1"
#     print("m2 response")
#     return response


# @app.middleware("http")
# async def m1(request: Request, call_next):
#     print("m1 request")
#     # if request.client.host in ["127.0.0.1",]:
#     #     return Response(content="visit forbidden")

#     # if request.url.path in ["/user"]:
#     #     return Response(content="visit forbidden")

#     start = time.time()
#     response = await call_next(request)
#     # response code
#     print("m1 response")
#     end = time.time()
#     response.headers["ProcessTime"] = f"{end-start}"

#     return response


if __name__ == '__main__':
    uvicorn.run("main:app", port=8080)
