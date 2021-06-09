from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from edaza import schemas, models, database

get_db = database.get_db


def createDrink( request: schemas.Drink, db: Session):
    created = models.Drink(
        
        title = request.title,
        prep = request.prep,
        cook = request.cook,
        total_time = request.total_time,
        yields = request.yields,
        no_of_recipe = request.no_of_recipe,
        tags = request.tags,
        indgridients = request.indgridients,
        level = request.level,
        rating = request.rating,
        drink_time = request.drink_time,
        drink_type = request.drink_type,
        description = request.description
    )
    db.add(created)
    db.commit()
    db.refresh(created)

    return created


def ShowDrinks(db: Session):
    all_drinks = db.query(models.Drink).all()
    return all_drinks

def ShowDrink(id, db: Session):
    single_drink = db.query(models.Drink).filter(models.Drink.id == id).first()
    return single_drink


def UpdateDrink(id, request: schemas.Drink, db: Session):
    updated = db.query(models.Drink).filter(models.Drink.id == id)
    updated.update(synchronize_session = False)
    db.commit()
    return 'updated successfully'

def DeleteDrink(id, db: Session):
    deleted = db.query(models.Drink).filter(models.Drink.id == id)
    deleted.delete(synchronize_session = False)
    db.commit()

    return 'deleted successfully'
