from fastapi import FastAPI
from middleware import log_middleware
from sqlmodel import SQLModel
from dbconfig import engine
from starlette.middleware.base import BaseHTTPMiddleware
import routes

app = FastAPI()

SQLModel.metadata.create_all(engine)

app.add_middleware(BaseHTTPMiddleware, dispatch = log_middleware)

app.include_router(routes.router)



