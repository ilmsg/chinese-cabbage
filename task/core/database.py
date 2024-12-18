from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, Session
from contextlib import contextmanager

sql_db = "sqlite:///:memory:"
engine = create_engine(sql_db, echo=True)

Base = declarative_base()

@contextmanager
def get_db():
    session = Session(bind=engine)
    try:
        yield session
    finally:
        session.close()
        