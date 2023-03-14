from fastapi import APIRouter
from models.user import User
from schemas.user import userEntity,usersEntity
from config.db import conn

user= APIRouter()

@user.get('/')
async def find_all_users():
    print(conn.local.user.find())
    print(usersEntity( conn.local.user.find()))
    return usersEntity( conn.local.user.find())
