from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import models
from database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

# Informações que devem ser inseridas para fazer a requisição da APÌ  

class ClassBase(BaseModel):
    classname: str

class UserBase(BaseModel):
    username: str
    
# Serve para não deixar a conexão aberta por muito tempo

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

# Utilizar o comando CREATE SCHEMA NOME_BANCO_DE_DADOS para criar um banco de dados e importar as tabelas definidas no models.py

@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserBase, db:db_dependency):
    user = models.User(**user.dict())
    db.add(user)
    db.commit()

@app.get("/users/{user_id}", status_code=status.HTTP_200_OK)
async def read_user(user_id: int, db:db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    return user

app.delete("/users/delete/{user_id}", status_code=status.HTTP_200_OK)
async def delete_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    db.delete(user)
    db.commit()

app.put("/users/edit/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, db: db_dependency):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail='Usuário não encontrado')
    
    db.add(user)
    db.commit()
