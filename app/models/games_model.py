from dataclasses import dataclass

from app.configs.database import db
from app.models import UserGame
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Game(db.Model):
    id: int
    name: str
    url_name: str

    __tablename__ = "games"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=True)
    url_name = Column(String(10), nullable=False, unique=True)

    champions = relationship("Champion", backpopulates="game")
    users = relationship("User", secondary=UserGame, backpopulates="games")
    teams = relationship("Team", backpopulates="game")
    positions = relationship("Position", backpopulates="game")
