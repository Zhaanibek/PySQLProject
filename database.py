import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

url_str = os.environ.get("url")
engine = create_engine(url_str)

metadata = MetaData()

Session = sessionmaker(bind=engine)
Base = declarative_base()
