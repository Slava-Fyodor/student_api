# schemas/student.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional


class StudentBase(BaseModel):
    name: str
    student_id: str
    grade: int
    email: EmailStr


class StudentCreate(StudentBase):
    pass


class StudentUpdate(StudentBase):
    name: Optional[str] = None
    grade: Optional[int] = None
    email: Optional[EmailStr] = None


class StudentInDB(StudentBase):
    id: int

    class Config:
        from_attributes = True