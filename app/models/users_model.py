from dataclasses import dataclass

from app.configs.database import db
from app.models import TeamUser, UserGame
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash


@dataclass
class User(db.Model):
    id: int
    name: str
    email: str
    bio: str

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    bio = Column(String)
    password = Column(String, nullable=True)

    positions = relationship(
        "Position", secondary="users_positions", back_populates="users"
    )

    champions = relationship(
        "Champion", secondary="users_champions", back_populates="users"
    )

    game = relationship("Game", secondary="users_games", back_populates="users")
    teams = relationship("Team", secondary="teams_users", back_populates="users")

    @property
    def password(self):
        raise AttributeError("Cannot access password")

    @password.setter
    def password(self, value):
        self.password = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password, password)
