from sqlalchemy import Integer, Column, String, ForeignKey
from typing import List
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database import Base

# models the reviews for SQL
class Review(Base):
    __tablename__= "review"
    id = Column(Integer, primary_key=True, index=True)
    review_description = Column(String)
    review_rating = Column(String)
    review_subject = Column(String)
    study_method = Column(String)
    teamwork = Column(Integer)
    exam_taking = Column(Integer)
    class_behavior = Column(Integer)
    overall_grade = Column(String)
    participation_level = Column(Integer)
    teacher_name = Column(String)
    student_id: Mapped[int] = mapped_column(ForeignKey("student.id"))
    student: Mapped["Student"] = relationship(back_populates="review_list")

# models the students for SQL
class Student(Base):
    __tablename__= "student"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    grade_num = Column(Integer)
    review_list: Mapped[List["Review"]] = relationship(back_populates="student")

    
