from dataclasses import dataclass

from app.configs.database import db
from app.models import TeamUser, UserGame
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    bio: str
    password: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    bio = Column(String)
    password = Column(String, nullable=False)

    positions = relationship(
        "Position", secondary="users_positions", back_populates="users"
    )

    champions = relationship(
        "Champion", secondary="users_champions", back_populates="users"
    )

    games = relationship("Game", secondary=UserGame, back_populates="users")
    teams = relationship("Team", secondary=TeamUser, back_populates="users")
