from ast import Delete
import secrets
import string

from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder

from src.auth.auth import AuthHandler
from .models import (StatusModel, TaskModel, DeleteStatusModel)
from .controllers import (
    add_status, 
    get_statuses, 
    add_task_by_id, 
    get_tasks, 
    delete_status
)

router = APIRouter()
auth_handler = AuthHandler()

@router.get('/all')
async def get_all(u_id=Depends(auth_handler.auth_wrapper)):
    res = await get_statuses(u_id)
    return {'data': res}


@router.get('/task')
async def get_tasks_by_status(status_id, u_id=Depends(auth_handler.auth_wrapper)):
    res = await get_tasks(status_id, u_id)
    return {'data': res}


@router.post('/task/add')
async def add_task(Task: TaskModel, status_id, u_id=Depends(auth_handler.auth_wrapper)):
    task = jsonable_encoder(Task)
    task["t_id"] = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(16))
    await add_task_by_id(task, status_id, u_id)
    return {'Task Added'}
    

@router.post('/status/add')
async def add_new(Status: StatusModel, u_id=Depends(auth_handler.auth_wrapper)):
    status = jsonable_encoder(Status)
    status['u_id'] = u_id
    res = await add_status(status)
    return {'data': res}


@router.post('/status/delete')
async def delete(DeleteModel: DeleteStatusModel):
    payload = jsonable_encoder(DeleteModel)
    res = await delete_status(payload["status_id"])
    return {'data': res}