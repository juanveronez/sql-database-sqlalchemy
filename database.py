from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, DeclarativeBase

import os
from dotenv import load_dotenv

# load_dotenv(dotenv_path='.env.dev')  # Carrega as variáveis de ambiente do arquivo .env
load_dotenv(dotenv_path='.env.prod')  # Carrega as variáveis de ambiente do arquivo .env

db_user = os.getenv("POSTGRES_USER")
db_password = os.getenv("POSTGRES_PASSWORD")
db_name = os.getenv("POSTGRES_DB")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")

# Configurando a conexão com o banco de dados
# DATABASE_URL = "postgresql://meu_usuario:minha_senha@localhost:5432/meu_banco"

DATABASE_URL = f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}?sslmode=require"
print(DATABASE_URL)

# Criando a engine de conexão
engine = create_engine(DATABASE_URL, connect_args={'sslmode': 'required'})

# Criando a sessão

Session = sessionmaker(bind=engine)

Base: DeclarativeBase = declarative_base()


# Definindo o modelo de dados
class Produto(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False)

class ProdutoBronze(Base):
    __tablename__ = "products_copper"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False)


# Criando a tabela
Base.metadata.create_all(bind=engine)
