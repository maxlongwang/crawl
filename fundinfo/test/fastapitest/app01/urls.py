from fastapi import APIRouter,Form

user=APIRouter()

@user.get("login")
def user_login():
    return {"user":"login"}


@user.post("/regin")
async def reg(username:str=Form(),password:str=Form()):
    return {"username":username}