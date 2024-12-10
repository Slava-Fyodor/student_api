# services/student.py
from sqlalchemy.orm import Session
from typing import List, Optional
from app.models.student import Student
from app.schemas.student import StudentCreate, StudentUpdate

class StudentService:
    @staticmethod
    async def create_student(db: Session, student: StudentCreate) -> Student:
        db_student = Student(**student.model_dump())
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    @staticmethod
    async def get_student(db: Session, student_id: int) -> Optional[Student]:
        return db.query(Student).filter(Student.id == student_id).first()

    @staticmethod
    async def get_students(db: Session, skip: int = 0, limit: int = 100) -> List[Student]:
        return db.query(Student).offset(skip).limit(limit).all()

    @staticmethod
    async def update_student(
        db: Session, student_id: int, student: StudentUpdate
    ) -> Optional[Student]:
        db_student = await StudentService.get_student(db, student_id)
        if db_student:
            update_data = student.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_student, field, value)
            db.commit()
            db.refresh(db_student)
        return db_student

    @staticmethod
    async def delete_student(db: Session, student_id: int) -> bool:
        db_student = await StudentService.get_student(db, student_id)
        if db_student:
            db.delete(db_student)
            db.commit()
            return True
        return False