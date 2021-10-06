from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

POSTGRES_DB = 'postgres'
POSTGRES_USER = 'postgres'
POSTGRES_PASSWORD = 'postgres'
DB_URI = 'postgresql://{}:{}@localhost:5432/{}'.format(POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_DB)

engine = create_engine(DB_URI, echo=True)
Session = sessionmaker(bind=engine)