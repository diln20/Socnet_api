from bson import ObjectId
from fastapi import APIRouter, status, Response
from bson import ObjectId
from passlib.hash import sha256_crypt
from starlette.status import HTTP_204_NO_CONTENT

from models.user import User
from config.db import conn
from schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get("/users", response_model=list[User], tags=["users"])
async def find_all_users():
    return usersEntity(conn.socnetv2.users.find())


@user.get("/verific/{email}", response_model=User, tags=["Login"])
async def find_user(email: str):
    consl = conn.socnetv2.users.find_one(({"email": email}))
    if consl == None:
        return consl
    else:
        return userEntity(consl)


@user.post("/users", response_model=User, tags=["SignUp"])
async def create_user(user: User):
    new_user = dict(user)
    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    del new_user["id"]
    id = conn.socnetv2.users.insert_one(new_user).inserted_id
    user = conn.socnetv2.users.find_one({"_id": id})
    return userEntity(user)


@user.get("/users/{id}", response_model=User, tags=["users"])
async def find_user(id: str):
    return userEntity(conn.socnetv2.users.find_one({"_id": ObjectId(id)}))


@user.put("/users/{id}", response_model=User, tags=["users"])
async def update_user(id: str, user: User):
    conn.socnetv2.users.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(user)})
    return userEntity(conn.socnetv2.users.find_one({"_id": ObjectId(id)}))


@user.delete("/users/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["users"])
async def delete_user(id: str):
    conn.socnetv2.users.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
