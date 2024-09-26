from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://drm722drwk72_user:jsSmJo5II5Yty5bPoF6zrXHoFi0N3FR5@dpg-crqiq968ii6s73cvgk8g-a.oregon-postgres.render.com/drm722drwk72" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
