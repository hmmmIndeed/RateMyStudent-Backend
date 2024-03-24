from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import DBModels.models
from database import engine
import studentAPI

# to use FastAPI
app = FastAPI()

# accessing frontend
origins = [
    "http://localhost:3000"
]

# used to connect frontend to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DBModels.models.Base.metadata.create_all(bind=engine)

# allows the router to work
app.include_router(studentAPI.router)