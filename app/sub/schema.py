from pydantic import BaseModel,EmailStr


class Post(BaseModel):
    email:str
    password:str
    

class postcreate(BaseModel):
    id:int
    email:str
    password:str
    pass


class post(BaseModel):
    id:int
    email:str
    password:str

    class Config:
        orm_mode=True


class user_create(BaseModel):
    email:EmailStr
    password:str


class userout(BaseModel):
    id:int
    email:EmailStr
    
    class Config:
        orm_mode=True
