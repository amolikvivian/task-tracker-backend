from fastapi import HTTPException, Depends
from src.database import db
from .auth import AuthHandler

users = db.get_collection("users")

auth_handler = AuthHandler()

async def register_user(user_details):
    user = users.find_one({"username": user_details["username"]})
    
    if(user is not None):
        return None

    hashed_password = auth_handler.get_password_hash(user_details["password"])
    payload = {
        "username": user_details["username"],
        "password": hashed_password
    }
    new_user = users.insert_one(payload)
    return user_helper(users.find_one({"_id": new_user.inserted_id}))

async def login_user(user_details):
    user = users.find_one({"username": user_details["username"]})
    if (user is None) or (not auth_handler.verify_password(user_details["password"], user['password'])):
        return None
    user = user_helper(user)
    token = auth_handler.encode_token(user["u_id"])
    return token, user

def user_helper(user) -> dict:
    return {
        "u_id": str(user["_id"]),
        "username": user["username"],
    }