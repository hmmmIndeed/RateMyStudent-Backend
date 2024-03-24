from fastapi import FastAPI, HTTPException, Depends, Query, Path
from fastapi.middleware.cors import CORSMiddleware


from APIModels.models import Student, Review, updatedStudent
from typing import List, Optional, Annotated

import DBModels.models

from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DBModels.models.Base.metadata.create_all(bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def base():
    return {"base"}

#Gets all the students
@app.get("/api/student")
async def get_all_students(db: Session = Depends(get_db)):
    return db.query(DBModels.models.Student).all()

@app.get("/api/student/review/{id}")
async def get_student_review(id : int, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if students == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )

    reviews = students.review_list

    if reviews == None:
        raise HTTPException(
            status_code=404,
            detail="reviews not found"
        )

    return reviews

@app.get("/api/student/{id}")
async def get_student_id(id : int, db: Session = Depends(get_db)):

    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    return student

#Gets all the students with the same first name
@app.get("/api/student/{first_name}")
async def get_first_students(first_name : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.first_name == first_name).all()


    return students 

#Gets all the students with the same last name
@app.get("/api/student/{last_name}")
async def get_last_students(last_name : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.last_name == last_name).all()

    return students 

@app.get("/api/student/{last_name}")
async def get_last_students(last_name : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.last_name == last_name).all()

    return students 

@app.get("/api/student/{id}/{subject}")
async def get_review_via_tags(id : int, subject : str, db: Session = Depends(get_db)):

    students = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    filtered_list = []

    for review in students.review_list:
        if review.review_subject == subject:
            filtered_list.append(review)


    return filtered_list

#
@app.post("/api/student/{first}/{last}/{grade}")
async def add_student(first : str, 
                      last : str, 
                      grade : int,
                      db : Session = Depends(get_db)):

    newStudent = Student(first_name=first, last_name=last, grade_number=grade)

    new_student = DBModels.models.Student()
    new_student.first_name = newStudent.first_name
    new_student.last_name = newStudent.last_name
    new_student.grade_num = newStudent.grade_number
    new_student.review_list = newStudent.review_list


    db.add(new_student)
    db.commit()
                                               
    return newStudent


#Updates a student's grade
#http://localhost:8000/api/student/1/foolishness/3/Writing/foolishness/5/3/2/4/sd/hehehe
@app.post("/api/student/{id}/{review_dec}/{review_rate}/{review_sub}/{method}/{work}/{exam}/{behavoir}/{participation}/{grade}/{teacher}")
async def add_review(id : int, review_dec : str, review_rate : int, review_sub : str, 
                     method : str, 
                     work : int, 
                     exam : int, 
                     behavoir : int, 
                     participation : int,
                     grade: str,
                     teacher : str,
                     db : Session = Depends(get_db)):

    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if student == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    
    new_review = DBModels.models.Review(review_description = review_dec,
    review_rating = review_rate,
    review_subject = review_sub,

    study_method = method,
    teamwork = work,
    exam_taking = exam,
    class_behavior = behavoir,
    participation_level = participation,

    overall_grade = grade,
    teacher_name = teacher,

    student_id= id)

    student.review_list.append(new_review)

    

    db.refresh(student)

    db.add(student)
    db.commit()

    return new_review
    
@app.put("/api/student/{id}/{review_id}/{new_text}")
async def edit_review(id : int, review_id : int, new_text : str,
                     db : Session = Depends(get_db)):

    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if student == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    
    
    new_review = None
    for review in student.review_list:
        if review.id == review_id:  # Assuming review has an 'id' attribute
            new_review = review
            break
    else:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    
    
    new_review.review_description = new_text

    student.review_list.append(new_review)

    db.refresh(student)

    db.add(student)
    db.commit()

    return new_review

@app.delete("/api/student/{id}")
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

@app.delete("/api/student/{id}/{post_id}")
async def delete_review(id :int, review_id : int, db : Session = Depends(get_db)):

    student = db.query(DBModels.models.Student).filter(DBModels.models.Student.id == id).first()

    if student == None:
        raise HTTPException(
            status_code=404,
            detail="student not found"
        )
    

    delete_review = None
    for review in student.review_list:
        if review.id == review_id:  
            delete_review = review
            break
    else:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )
    
    student.review_list.remove(delete_review)

    #db.refresh(student)

    #db.commit()
    
    return {"Popped Review!!!!! :3"}
    
