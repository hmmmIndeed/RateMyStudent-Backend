from typing import Optional, List
from pydantic import BaseModel

# contains the reviews and their details
class Review(BaseModel):
    review_description: str
    review_rating: int
    review_subject: Optional[str]
    study_method : str 
    teamwork : int
    exam_taking : int
    class_behavior : int
    participation_level : int
    overall_grade : str
    teacher_name : str

# contains students and their details
class Student(BaseModel):
    first_name: str
    last_name: str
    grade_number: int
    review_list: Optional[List[Review]] = []

# used to add reviews
class updatedStudent(BaseModel):
    
    new_review : str


