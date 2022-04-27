from fastapi import APIRouter, Depends, HTTPException
from fastapi.encoders import jsonable_encoder

from .auth import AuthHandler
from .models import UserModel
from .controllers import (register_user, login_user)

router = APIRouter()

auth_handler = AuthHandler()

@router.post('/register')
async def register(User: UserModel):
    user = jsonable_encoder(User)
    new_user = await register_user(user)
    if(new_user is None):
        raise HTTPException(status_code=401, detail='Username already taken')
    else:
        return {"data": new_user}


@router.post('/login')
async def login(User: UserModel):
    user = jsonable_encoder(User)
    token, user = await login_user(user)
    print(user)
    if(token is None):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    else:
        return {'type': "Bearer" ,'token': token }