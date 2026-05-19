from fastapi import FastAPI
from pydantic import BaseModel
from myModel import u
app = FastAPI()

class User(BaseModel):
    name: str
    age: int

@app.get("/user")
def create_user(user: User):
    return {
        "name": u.name,
        "age": u.age
    }