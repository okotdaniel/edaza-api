from fastapi import FastAPI, APIRouter, Depends
from sqlalchemy.orm import Session
from edaza.api import Drink
from edaza import schemas, models, database


get_db = database.get_db

router = APIRouter(
    tags=['Drink']
)

@router.post('/drink/')
def AddDrink(request: schemas.Drink, db: Session = Depends(get_db)):
    return Drink.createDrink(request, db)

@router.get('/drinks/')
def GetDrinks(  db: Session = Depends(get_db)):
    return Drink.ShowDrinks( db)


@router.get('/drink/{id}')
def GetDrink(id:int,  db: Session = Depends(get_db)):
    return Drink.ShowDrink(id, db)


@router.put('/drink/{id}')
def update_drink(id:int,  db: Session = Depends(get_db)):
    return Drink.UpdateDrink(id, db)

@router.delete('/drink/{id}')
def delete_drink(id:int, db: Session = Depends(get_db)):
    return Drink.DeleteDrink(id, db)

