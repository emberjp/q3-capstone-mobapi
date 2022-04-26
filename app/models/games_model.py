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
    name = Column(String)
    url_name = Column(String)

    champions = relationship("Champion", backpopulates="game")
    users = relationship("User", secondary=UserGame, backpopulates="games")
