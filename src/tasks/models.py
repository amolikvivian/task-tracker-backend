from pydantic import BaseModel
from typing import Optional, List

class TaskModel(BaseModel):
    t_id: Optional[str]
    title: str
    desc: str

class StatusModel(BaseModel):
    label: str
    bgColor: str
    textColor: str
    u_id: Optional[str]
    tasks: List[TaskModel] = []

class DeleteStatusModel(BaseModel):
    status_id: str

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }