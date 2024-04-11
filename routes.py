from fastapi import APIRouter, File, UploadFile, Response, Depends, Form
from sqlmodel import Session
from deps import get_session
from pydantic import EmailStr
from typing import Annotated
from fastapi.responses import RedirectResponse
from controllers import create_user




router = APIRouter()




@router.get('/')
async def root():
    return RedirectResponse('/docs')







@router.post('/register')
async def register_user(name: Annotated[str, Form(title="Name", example="John Doe", description="Enter your name", pattern="^[a-zA-Z\s]+$")], age: Annotated[int, Form(title="Age", example=30, description="Enter your age")], email: Annotated[EmailStr, Form(title="Email Address", example="vVJc0@example.com", description="Enter your email address")], response: Response, session: Annotated[Session, Depends(get_session)], photo: UploadFile = File(default=None)):
    data = create_user(name, age, email, session, photo)
    if "error" in data:
        response.status_code = 400
        return data
    response.status_code = 201
    return data