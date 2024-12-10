# api/v1/endpoints/students.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.student import StudentCreate, StudentUpdate, StudentInDB
from app.services.student import StudentService
from app.api.deps import get_db

router = APIRouter()

@router.post("/", response_model=StudentInDB)
async def create_student(
    student: StudentCreate,
    db: Session = Depends(get_db)
):
    return await StudentService.create_student(db, student)

@router.get("/{student_id}", response_model=StudentInDB)
async def read_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    student = await StudentService.get_student(db, student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

@router.get("/", response_model=List[StudentInDB])
async def read_students(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return await StudentService.get_students(db, skip, limit)

@router.put("/{student_id}", response_model=StudentInDB)
async def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    updated_student = await StudentService.update_student(db, student_id, student)
    if updated_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return updated_student

@router.delete("/{student_id}")
async def delete_student(
    student_id: int,
    db: Session = Depends(get_db)
):
    success = await StudentService.delete_student(db, student_id)
    if not success:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}