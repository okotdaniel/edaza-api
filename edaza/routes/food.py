from fastapi import APIRouter, Depends
from edaza.api import Food
from edaza  import schemas, models, database
from sqlalchemy.orm import Session

router = APIRouter()

get_db = database.get_db

@router.post('/foods', tags=['food'])
def addFood(request: schemas.Food, db: Session = Depends(get_db) ):
    return Food.CreateFood(request, db)

@router.get('/food/', tags=['food'])
def getFoods( db: Session = Depends(get_db) ):
    return Food.ShowFoods(db)

@router.get('/food/{id}', tags=['food'])
def getFood(id, db: Session = Depends(get_db) ):
    return Food.ShowFood(id, db)

@router.put('/food/{id}', tags=['food'])
def updateFood(id, request: schemas.Food, db: Session = Depends(get_db) ):
    return Food.UpdateFood(id, request, db)

@router.delete('/food/{id}', tags=['food'])
def deleteFood(id, db: Session = Depends(get_db) , status_code=203):
    return Food.DeleteFood(id, db)