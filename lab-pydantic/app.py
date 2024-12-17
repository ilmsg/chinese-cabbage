from typing import List
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, Session
from pydantic import BaseModel, ConfigDict
import random

# db_url = "sqlite:///mydatabase.sqlite"
db_url = "sqlite:///:memory:"
engine = create_engine(db_url, echo=True)

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement="auto")
    name = Column(String)
    age = Column(Integer)
    
    def __repr__(self) -> str:
        return f"<User(name={self.name}, age={self.age})>"
    
Base.metadata.create_all(engine)
session = Session(bind=engine)

# 
names_list = ["ali", "shaharm", "mohamad", "jafar", "sasan"]
for name in names_list:
    new_user = User(name=name, age=random.randint(30, 40))
    session.add(new_user)
session.commit()

users: List[User] = session.query(User).all()
for user in users:
    print(user)
    
class UserSchema(BaseModel):
    id: int
    name: str
    age: int
    
    model_config = ConfigDict(from_attributes=True)
    
user_from_db = session.query(User).filter(User.id == 5).one_or_none()

user_schema = UserSchema.model_validate(user_from_db)
print(user_schema.name)

