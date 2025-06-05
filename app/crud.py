from sqlalchemy.orm import Session
from . import models, schemas

# Create a new user
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        name=user.name,
        age=user.age,
        height=user.height,
        weight=user.weight
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Get a user by ID
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# Get all users
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

# Create fitness record for a user
def create_fitness_record(db: Session, record: schemas.FitnessRecordCreate, user_id: int):
    db_record = models.FitnessRecord(
        user_id=user_id,
        date=record.date,
        steps=record.steps,
        calories_burned=record.calories_burned,
        workout_minutes=record.workout_minutes
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# Get fitness records for a user
def get_fitness_records(db: Session, user_id: int):
    return db.query(models.FitnessRecord).filter(models.FitnessRecord.user_id == user_id).all()
