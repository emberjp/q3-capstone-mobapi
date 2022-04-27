from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Team(db.Model):
    id: int
    name: str

    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)

    users = relationship("User", secondary="TeamUser", back_populates="teams")
    game = relationship("Game", back_populates="teams", uselist=False)
