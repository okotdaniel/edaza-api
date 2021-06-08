from fastapi import FastAPI, APIRouter
from edaza  import schemas, models, database
from edaza.routes import food


app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)


#routes 
app.include_router(food.router)
