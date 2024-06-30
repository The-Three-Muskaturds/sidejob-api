import os
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Create the URL from env -> username, password, host, port, name
#https://docs.sqlalchemy.org/en/20/core/engines.html

db_url = URL.create(
    drivername="postgresql+psycopg2",
    username=os.getenv("DB_USER", "defaultuser"),
    password=os.getenv("DB_PWD", "password"),
    host=os.getenv("DB_HOST", "localhost"),
    port=os.getenv("DB_PORT", "5432"),
    database=os.getenv("DB_NAME", "sidejob_db"),
)

engine = create_engine(db_url)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind=engine)

Base = declarative_base()