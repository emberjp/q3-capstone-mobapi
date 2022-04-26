from dataclasses import dataclass

from app.configs.database import db
from app.models import TeamUser, UserGame, users_champions, users_positions
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class User(db.Model):
    id: int
    name: str
    bio: str
    password: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    bio = Column(String)
    password = Column(String, nullable=False)

    positions = relationship(
        "Position", secondary=users_positions, backpopulates="users"
    )

    champions = relationship(
        "Champion", secondary=users_champions, backpopulates="users"
    )

    games = relationship("Game", secondary=UserGame, backpopulates="users")
    teams = relationship("Team", secondary=TeamUser, backpopulates="users")
