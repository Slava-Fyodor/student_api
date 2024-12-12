# api/v1/router.py
from fastapi import APIRouter
from app.api.v1.endpoints import students, courses

api_router = APIRouter()

api_router.include_router(students.router, prefix="/students", tags=["students"])
api_router.include_router(courses.router, prefix="/courses", tags=["courses"])