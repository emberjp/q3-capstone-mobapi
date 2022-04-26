from sqlalchemy import Column, Integer, String
from dataclasses import dataclass

from app.configs.database import db


@dataclass
class User(db.Model):
    id: int
    name: str
    bio: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False, unique=True)
    bio = Column(String)
