from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship


@dataclass
class Position(db.Model):
    id: int
    name: str

    __tablename__ = "positions"

    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    game_id = Column(Integer, ForeignKey("games.id"))
    users = relationship(
        "User", secondary="users_positions", back_populates="positions"
    )
    
