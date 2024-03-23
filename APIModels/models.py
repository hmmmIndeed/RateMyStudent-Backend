from typing import Optional, List
from pydantic import BaseModel

class Review(BaseModel):
    review_description: str
    review_rating: int
    review_subject: Optional[str]


class Student(BaseModel):
    first_name: str
    last_name: str
    #password: str
    review : str
    
    grade_number: int
    review_list: Optional[List[Review]] = []

class updatedStudent(BaseModel):

    #grade_number: Optional[int]
    new_review : str


