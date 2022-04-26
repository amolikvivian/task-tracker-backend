from pydantic import BaseModel, EmailStr
from typing import Optional

class UserModel(BaseModel):
    username: str
    password: str

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }