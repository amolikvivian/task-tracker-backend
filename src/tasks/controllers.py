from src.database import db
from bson.objectid import ObjectId

statuses = db.get_collection("statuses")

async def get_statuses(u_id):
    status_list = []
    cursor = statuses.find({"u_id": u_id})
    for x in cursor:
        status_list.append(status_builder(x))
    return status_list


async def add_task_by_id(task, status_id, u_id):
    status = statuses.find_one({"_id": ObjectId(status_id), "u_id": u_id})
    task_list = status['tasks']
    task_list.append(task)
    updated = statuses.update_one({"u_id": u_id, "_id": ObjectId(status_id)}, {"$set": {"tasks": task_list}})
    return updated
    

async def get_tasks(status_id, u_id):
    status = statuses.find_one({"_id": ObjectId(status_id), "u_id": u_id})
    return status["tasks"]


async def add_status(status):
    status = statuses.insert_one(status)
    new_status = statuses.find_one({"_id": status.inserted_id})
    return status_builder(new_status)

async def delete_status(status_id):
    statuses.delete_one({"_id": ObjectId(status_id)})
    return 'Deleted'

def status_builder(status)-> dict:
    return {
        "id": str(status["_id"]),
        "bgColor": status["bgColor"],
        "textColor": status["textColor"],
        "u_id": status["u_id"],
        "tasks": status["tasks"]
    }