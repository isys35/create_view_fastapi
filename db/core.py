import pathlib

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

PATH_TO_ENV_FILE = os.path.join(pathlib.Path(__file__).parent.parent, '.env')
load_dotenv(PATH_TO_ENV_FILE)

POSTGRES_DB = os.getenv('POSTGRES_DB')
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
DB_URI = 'postgresql://{}:{}@localhost:5432/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)