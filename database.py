from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# mysql+pymysql://root:senha!@localhost:3306/nomeDoBancoDeDados

URL_DATABASE = 'mysql+pymysql://root@localhost:3306/teste'

engine = create_engine(URL_DATABASE)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Rodar no terminal uvicorn main:app --reload para executar o servidor e fazer as requisições, é necessário também para rodar localmente rodar o XAMPP ou USBwebserver

# Para checar a documentação criada pelo swagger http://127.0.0.1:8000/docs ou http://127.0.0.1:8000/redoc