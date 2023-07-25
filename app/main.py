from fastapi import FastAPI,Response,status,HTTPException,Depends
from random import randrange
from  psycopg2.extras import RealDictCursor
from sub import models,schema
from sub.databasse import engine,get_db
from  sqlalchemy.orm import Session
from passlib.context import CryptContext
from fastapi.middleware.cors import CORSMiddleware

pwd_context=CryptContext(schemes=["argon2"],deprecated="auto")

models.Base.metadata.create_all(bind=engine)

app=FastAPI()
origins = [    
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def login():

    return{"message":"hell0 "}


@app.get("/sqlalchemy")
def test_db(db: Session = Depends(get_db)):
    post=db.query(models.Post)
    print(post)
    return{"data":"success"}




@app.post("/user",status_code=201,response_model=schema.userout)
def create_user(user:schema.user_create,db:Session = Depends(get_db)):


    password_hased=pwd_context.hash(user.password)
    user.password=password_hased

    new_user=models.user(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)



    return new_user

def authenticate_user(username: str, password: str, db: Session):
    from model import user
    user = db.query(User).filter(User.username == username).first()
    if user and pwd_context.verify(password, user.password):
        return user
    return None


@app.post("/login")
def login(username: str, password: str, db: Session = Depends(get_db)):
    user = authenticate_user(username, password, db)
    if user:
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(data={"sub": user.username}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer", "username": user.username}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )