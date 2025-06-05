from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import engine, SessionLocal
from .ml_model import model  # Import ML model
from pydantic import BaseModel
import numpy as np

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency — get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Health & Fitness Tracker API is running 🚀"}

# Create a new user
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

# Get all users
@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_users(db=db, skip=skip, limit=limit)

# Get a user by ID
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Create fitness record
@app.post("/users/{user_id}/fitness_records/", response_model=schemas.FitnessRecord)
def create_record_for_user(user_id: int, record: schemas.FitnessRecordCreate, db: Session = Depends(get_db)):
    return crud.create_fitness_record(db=db, record=record, user_id=user_id)

# Get fitness records for a user
@app.get("/users/{user_id}/fitness_records/", response_model=list[schemas.FitnessRecord])
def get_fitness_records(user_id: int, db: Session = Depends(get_db)):
    return crud.get_fitness_records(db=db, user_id=user_id)

# ===== ML Prediction Endpoint =====

class PredictionRequest(BaseModel):
    days: int

@app.post("/predict_calories/")
def predict_calories(req: PredictionRequest):
    X_new = np.array([[req.days]])
    prediction = model.predict(X_new)
    return {"predicted_calories": prediction[0]}
