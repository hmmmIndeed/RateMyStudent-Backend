from fastapi import FastAPI, HTTPException, Depends, APIRouter
from fastapi.middleware.cors import CORSMiddleware


from APIModels.models import Student, Review, updatedStudent
from typing import List, Optional

import DBModels.models

from database import engine, SessionLocal
from sqlalchemy.orm import Session

from backend import get_db

router = APIRouter()


#Gets all the students
@router.get("/api/student")
async def get_all_students(db: Session = Depends(get_db)):
    return db.query(DBModels.models.Student).all()

@router.get("/api/student/{id}")
async def get_student_review(id : int, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    reviews = students.review_list

    return reviews


#Gets all the students with the same first name
@router.get("/api/student/{first_name}")
async def get_first_students(first_name : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.first_name == first_name).all()

    return students 

#Gets all the students with the same last name
@router.get("/api/student/{last_name}")
async def get_last_students(last_name : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.last_name == last_name).all()

    return students 


#
@router.post("/api/student/{first}/{last}/{grade}/{review}")
async def add_student(first : str, last : str, grade : int, review : str, db : Session = Depends(get_db)):

    
    newStudent = Student(first_name=first, last_name=last, grade_number=grade, review=review)

    new_student = DBModels.models.Student()
    new_student.first_name = newStudent.first_name
    new_student.last_name = newStudent.last_name
    new_student.review = newStudent.review
    new_student.grade_num = newStudent.grade_number
    new_student.review_list = newStudent.review_list


    db.add(new_student)
    db.commit()
                                               
    return newStudent


#Updates a student's grade
@router.put("/api/student/{id}/{review_dec}/{review_rate}/{review_sub}")
async def add_review(id : int, review_dec : str, review_rate : int, review_sub : str, db : Session = Depends(get_db)):

    #aStudent = updatedStudent(new_review=reviews)

    #updates the student here
    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if student == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    
    new_review = DBModels.models.Review(review_description = review_dec,
    review_rating = review_rate,
    review_subject = review_sub,
    student_id= id)

    #return new_review

    student.review_list.append(new_review)

    

    db.refresh(student)

    db.add(student)
    db.commit()

    return student
    

@router.delete("/api/student/{id}")
async def delete_student(id : int, db : Session = Depends(get_db)):

    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if student == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )


    db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).delete()

    db.commit()
    
    return {"successful"}

