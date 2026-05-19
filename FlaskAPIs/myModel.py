from pydantic import BaseModel

class User(BaseModel):
  name:str
  age:int

u = User(name = "Priyabrata", age = 25)

print(u)