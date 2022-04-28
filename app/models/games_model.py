from dataclasses import dataclass

from app.configs.database import db
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

    champions = relationship("Champion", back_populates="game")
    users = relationship("User", secondary="users_games", back_populates="game")
    teams = relationship("Team", back_populates="game")
    positions = relationship("Position", back_populates="game")
