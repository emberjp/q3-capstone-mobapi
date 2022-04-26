from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String


@dataclass
class UserGame(db.Model):
    id: int
    nickname = str
    rank = str

    __tablename__ = "users_games"

    id = Column(Integer, primary_key=True)
    nickname = Column(String)
    rank = Column(String)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id"), nullable=False)
