from dataclasses import dataclass

from app.configs.database import db

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Role(db.Model):
    id: int
    name: str

    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String(16))

    champions = relationship(
        "Champion", secondary="champions_roles", back_populates="roles"
    )
