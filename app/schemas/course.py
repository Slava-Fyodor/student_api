# schemas/course.py
from pydantic import BaseModel
from typing import List, Optional


class CourseBase(BaseModel):
    name: str
    code: str
    credit: int


class CourseCreate(CourseBase):
    pass


class CourseUpdate(CourseBase):
    name: Optional[str] = None
    credit: Optional[int] = None


class CourseInDB(CourseBase):
    id: int

    class Config:
        from_attributes = True