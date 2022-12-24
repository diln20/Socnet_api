import email
from turtle import pos
from unicodedata import name
from bson import ObjectId
from fastapi import APIRouter, status, Response
from bson import ObjectId

from starlette.status import HTTP_204_NO_CONTENT
from schemas.user import userEntity
from models.post import Post
from config.db import conn
from schemas.post import postEntity, postEntity, postsEntityA
from models.user import User

post = APIRouter()


@post.get("/posts", response_model=list[Post], tags=["posts"])
async def find_all_posts():
    # print(list(postsEntity(conn.socnetv2.posts.find())))
    pipeline = [
        {
            "$lookup": {
                "from": "users",
                "localField": "usr",
                "foreignField": "email",
                "as": "author",
            },
        },
    ]
    cons = conn.socnetv2.posts.aggregate(pipeline)

    return postsEntityA(cons)


@post.get("/posta/{id}", response_model=list[Post], tags=["posts user"])
async def load_messages_from_user(user: str):
    # print(list(postsEntity(conn.socnetv2.posts.find())))
    pipeline = [
        {"$match": {"email": user}},
        {
            "$lookup": {
                "from": "users",
                "localField": "usr",
                "foreignField": "email",
                "as": "author",
            },
        },
    ]
    cons = conn.socnetv2.posts.aggregate(pipeline)

    return postsEntityA(cons)


@post.post("/posts", response_model=Post, tags=["Crear Post"])
async def create_post(post: Post):
    new_post = dict(post)
    del new_post["id"]

    id = conn.socnetv2.posts.insert_one(new_post).inserted_id
    post = conn.socnetv2.posts.find_one({"_id": id})
    return postEntity(post)


@post.delete(
    "/posts/{id}", status_code=status.HTTP_204_NO_CONTENT, tags=["post delete"]
)
async def delete_post(id: str):
    conn.socnetv2.posts.find_one_and_delete({"_id": ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)


@post.put("/posts/{id}", response_model=Post, tags=["post"])
async def update_post(id: str, post: Post):
    new_update = dict(post)
    del new_update["id"]
    conn.socnetv2.posts.find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": new_update},
    )
    return postEntity(conn.socnetv2.posts.find_one({"_id": ObjectId(id)}))


@post.get("/post/{id}", response_model=Post, tags=["posts"])
async def find_post(id: str):
    return postEntity(conn.socnetv2.posts.find_one({"_id": ObjectId(id)}))
