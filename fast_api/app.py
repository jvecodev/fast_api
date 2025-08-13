# fast_api/app.py
from fastapi import FastAPI, HTTPException
from http import HTTPStatus
from pymongo import ReturnDocument
from bson import ObjectId

from fast_api.schema import Message, UserSchema, UserPublic, UserList
from fast_api.db import db, to_object_id, serialize_user

app = FastAPI(title="FastAPI Example")

@app.get("/", status_code=HTTPStatus.OK, response_model=Message)
async def read_root():
    return {"message": "Hello World"}

@app.get("/second/", status_code=HTTPStatus.OK, response_model=Message)
async def second_function():
    return {"message": "Hello World 2"}

@app.post("/user/", status_code=HTTPStatus.CREATED, response_model=UserPublic)
async def create_user(user: UserSchema):
    payload = user.model_dump()
    result = await db.users.insert_one(payload)
    doc = await db.users.find_one({"_id": result.inserted_id})
    return serialize_user(doc)

@app.get("/user/", response_model=UserList)
async def get_users():
    cursor = db.users.find({})
    users = []
    async for doc in cursor:
        users.append(serialize_user(doc))
    return {"users": users}

@app.put("/user/{user_id}", response_model=UserPublic)
async def update_user(user_id: str, user: UserSchema):
    try:
        oid = to_object_id(user_id)
    except ValueError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")

    updated = await db.users.find_one_and_update(
        {"_id": oid},
        {"$set": user.model_dump()},
        return_document=ReturnDocument.AFTER,
    )
    if not updated:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")
    return serialize_user(updated)

@app.delete("/user/{user_id}", response_model=UserPublic, status_code=HTTPStatus.OK)
async def delete_user(user_id: str):
    try:
        oid = to_object_id(user_id)
    except ValueError:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")

    deleted = await db.users.find_one_and_delete({"_id": oid})
    if not deleted:
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND, detail="Usuário não encontrado")
    return serialize_user(deleted)
