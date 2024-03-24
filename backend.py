from fastapi import FastAPI, HTTPException, Depends, Query, Path
from fastapi.middleware.cors import CORSMiddleware


from APIModels.models import Student, Review, updatedStudent
from typing import List, Optional, Annotated

import DBModels.models

from database import engine, SessionLocal
from sqlalchemy.orm import Session

import studentAPI

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

app.include_router(studentAPI.router)

@app.get("/")
async def base():
    return {"base"}
