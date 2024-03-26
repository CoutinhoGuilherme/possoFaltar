from sqlalchemy import Boolean, Column, Integer, String
from database import Base

# Criação das tabelas

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True)

class schoolClasses(Base):
    __tablename__ = 'schoolClasses'

    id = Column(Integer, primary_key=True, index=True)
    classname = Column(String(50))
    
    
