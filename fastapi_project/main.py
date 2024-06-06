import models
from fastapi import FastAPI, Depends, HTTPException 
from sqlalchemy.orm import Session 
import crud, schemas
from database import engine, SessionLocal
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

models.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
     yield db
    finally:
     db.close()

app = FastAPI()

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
 db_user = crud.get_user_by_email(db, email=user.email)
 if db_user:
    raise HTTPException(status_code=400, detail="Email już zarejestrowany")
 return crud.create_user(db=db, user=user)


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
 db_user = crud.get_user(db, user_id=user_id)
 if db_user is None:
    raise HTTPException(status_code=404, detail="Użytkownik nie znaleziony")
 return db_user[0]


@app.get("/")
async def root():
 return {"message": "Test obrazu"}
