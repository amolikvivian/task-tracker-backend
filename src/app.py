from fastapi import FastAPI

from .auth.routes import router as AuthRouter
from .tasks.routes import router as TaskRouter

app = FastAPI()

app.include_router(AuthRouter, tags=["Auth"], prefix="/auth")
app.include_router(TaskRouter, tags=["Tasks"])
