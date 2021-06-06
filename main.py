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

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

#user routes 
@app.get("/users/", tags=['user'])
def getUsers():
    return {"users": "users here"}

@app.post("/users/{user_id}", tags=['user'])
def postUser(user_id):
    return {"message": "account created  successfully"}

@app.put("/user/{user_id}", tags=['user'])
def updateUser(user_id):
    return {"message": "user updated successfully"}

@app.delete("/user/{user_id}", tags=['user'])
def deleteUser(user_id):
    return {"message": "user deleted successfully "}

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
def updateFood(db: Session = Depends(get_db), tags=['food']):
    food = db.query(models.Food).filter(models.Food.id == id ).first().update()

@app.delete('/food/{id}')
def deleteFood(id, db: Session = Depends(get_db), tags=['food'], status_code=203):
    food = db.query(models.Food).filter(models.Food.id == id ).delete()