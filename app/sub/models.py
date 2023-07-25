from .databasse import Base
from sqlalchemy import Column, Integer, String, Boolean,TIMESTAMP,text,VARCHAR
from sqlalchemy.sql.expression import null
from sqlalchemy.ext.declarative import declarative_base
import time
class Post(Base):
    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, nullable=False,autoincrement=True)
    email = Column(String(25), primary_key=True, nullable=False)
    password = Column(String(25), nullable=False)

class user(Base):
    __tablename__="users"
    id = Column(Integer, primary_key=True, nullable=False)
    email=Column(String(25),nullable=False,unique=True)
    password=Column(VARCHAR(500000),nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
