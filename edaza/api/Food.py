from fastapi import FastAPI, Depends
from typing import Optional
from sqlalchemy.orm import Session
from edaza import schemas, models, database

get_db = database.get_db


def CreateFood(request: schemas.Food, db: Session ):
    added_food = models.Food(
        name =request.name,
        picture = request.picture,
        type = request.type,
        category = request.category,
        mode_of_preparation = request.mode_of_preparation
        )

    db.add(added_food)
    db.commit()
    db.refresh(added_food)

    return added_food


def ShowFood(id, db: Session ):
    single_food = db.query(models.Food).filter(models.Food.id == id ).first()
    return single_food

def ShowFoods( db: Session ):
    all_foods = db.query(models.Food).all()
    return all_foods
   
def UpdateFood(id, request: schemas.Food, db: Session ):
    food = db.query(models.Food).filter(models.Food.id == id )
    food.update(request, synchronize_session='evaluate')
    db.commit()
    return {"food updated successfully"}

def DeleteFood(id, db: Session ):
    food = db.query(models.Food).filter(models.Food.id == id )
    food.delete(synchronize_session=False)
    db.commit()
    return {"message": "deleted successfully"}