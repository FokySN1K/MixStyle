from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from  sqlalchemy.dialects.sqlite import insert
from sqlalchemy.ext.declarative import declarative_base

#sqlite_database = "sqlite:///DataBase/MixStyle.db"
sqlite_database = "sqlite:///../DataBase/MixStyle.db"
engine = create_engine(sqlite_database, echo=False)

session = Session(bind=engine)
