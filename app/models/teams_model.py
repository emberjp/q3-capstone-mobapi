from dataclasses import dataclass

from app.configs.database import db

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Team(db.Model):
    id: int
    name: str
    game: dict
    __tablename__ = "teams"

    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)

    game_id = Column(Integer, ForeignKey("games.id"))

    users = relationship("User", secondary="teams_users", back_populates="teams")
    game = relationship("Game", back_populates="teams", uselist=False)
