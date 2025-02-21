from fastapi import APIRouter, File, UploadFile
from pydantic import BaseModel, Field, field_validator
from typing import List, Union, Optional
from datetime import date
test = APIRouter()


class Addr(BaseModel):
    province: str
    city: str


class User(BaseModel):
    # name: str = "root"
    # name:str=Field(pattern="^a")
    name: str
    age: int = Field(default=0, gt=0, lt=100)
    birth: Union[date, None] = None
    friends: List[int] = []
    descrition: Optional[str] = None
    addr: Addr

    @field_validator("name")
    def name_must_alpha(cls, value):
        assert value.isalpha(), 'name must bu alpha'
        return value


class Data(BaseModel):
    data: List[User]


@test.get("/", tags=["get test"], summary="get test summary", deprecated=True)
async def home_old():
    return {"user_id": 1001}


@test.get("/get", tags=["get test"], summary="get test summary")
async def home():
    return {"user_id": 1001}


@test.get("/user/{user_id}", tags=["get test"], summary="get test summary")
async def get_user(user_id):
    return {"user_id": user_id}


@test.post("/user", tags=["post test"], summary="post test summary")
async def post_data(user: User):
    print(user, type(user))
    return user


@test.post("/data")
async def data(data: Data):
    return data


@test.put("/put", tags=["put test"], summary="put test summary")
async def put_test():
    return {"user_id": "put 1001"}


@test.delete("/delete", tags=["delete test"], summary="delete test summary")
async def delete_test():
    return {"user_id": "delete 1001"}


# file load ,small file
@test.post("/file", tags=["upload  file"], summary="upload small file")
async def get_file(file: bytes = File()):
    print("file", file)
    return {"file": len(file)}


@test.post("/files", tags=["upload  file"], summary="upload small file")
async def get_files(files: List[bytes] = File()):
    # print("file",files)
    for file in files:
        print(len(file))
    return {"file": len(files)}


@test.post("/uplodafile", tags=["upload large file"], summary="upload small file")
async def get_file2(file: UploadFile):
    print("file", file)
    # file copy to folder
    path = os.path.join("imgs", file.filename)
    with open(path, 'wb') as f:
        for line in file.file:
            f.write(line)

    return {"file": file.filename}


@test.post("/uploadfiles")
async def getUploadFiles(files: List[UploadFile]):
    print("file", files)
    return {"names": [file.filename for file in files]}
