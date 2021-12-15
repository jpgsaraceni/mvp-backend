import os
from dotenv import load_dotenv
from databases import Database
from sqlalchemy.schema import CreateSchema
from sqlalchemy import create_engine, MetaData
from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Integer,
    String,
    Table,
    Text
)
from sqlalchemy.sql import func

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
DB_SCHEMA = os.getenv('DB_SCHEMA')

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL) # used for communicating with the database

if not engine.dialect.has_schema(engine, DB_SCHEMA):
    engine.execute(CreateSchema(DB_SCHEMA))

metadata = MetaData(schema=DB_SCHEMA) # used for creating the database schema

# define table products
products = Table (
    'products',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('description', String(140), nullable=False),
    Column('price', Float, nullable=False),
    Column('image', Text, nullable=True),
    Column('created_at', DateTime(timezone=True), default=func.now(), nullable=False),
    Column('updated_at', DateTime(timezone=True)),
    Column('deleted_at', DateTime(timezone=True)),
)

# create table products on the database
metadata.create_all(engine)

# database query builder
database = Database(DATABASE_URL)
