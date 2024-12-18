from fastapi import FastAPI
from core.database import engine
from model.task import Base

Base.metadata.create_all(engine)

app = FastAPI(title="TODO API", version="1.0.0")

