from typing import Optional
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from edaza  import schemas, models, actions, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#ingridient routes 

@app.post('/foods')
def addFood(request: schemas.Food, db: Session = Depends(get_db), tags=['food']):
    added_food = models.Food(
        name =request.name,
        picture = request.picture,
        type = request.type,
        category = request.category,
        mode_of_preparation = request.mode_of_preparation)

    db.add(added_food)
    db.commit()
    db.refresh(added_food)

    return added_food

@app.get('/food')
def getFood(db: Session = Depends(get_db), tags=['food']):
    all_foods = db.query(models.Food).all()
    return all_foods

@app.get('/food/{id}')
def getFoodById(id, db: Session = Depends(get_db), tags=['food']):
    single_food = db.query(models.Food).filter(models.Food.id == id ).first()
    return single_food

@app.put('/food/{id}')
def updateFood(request: schemas.Food, db: Session = Depends(get_db), tags=['food']):
    food = db.query(models.Food).filter(models.Food.id == id ).first()
    food.update(request)
    db.commit()
    return {"food updated successfully"}

@app.delete('/food/{id}')
def deleteFood(id, db: Session = Depends(get_db), tags=['food'], status_code=203):
    food = db.query(models.Food).filter(models.Food.id == id )
    food.delete(synchronize_session=False)
    db.commit()
    return {"message": "deleted successfully"}