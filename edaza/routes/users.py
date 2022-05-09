#added imports
from typing import Optional
from fastapi import FastAPI

#added
app = FastAPI()

#test route
@app.get("/")
async def test():
    return {"msg": "Welcome"}



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
