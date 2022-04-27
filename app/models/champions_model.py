from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


@dataclass
class Champion(db.Model):
    id: int
    name: str
    img_url: str
    info: str

    __tablename__ = "champions"

    id = Column(Integer, primary_key=True)
    name = Column(String(16), nullable=False)
    img_url = Column(String, nullable=False)
    info = Column(String, nullable=False)

    game_id = Column(Integer, ForeignKey("games.id"))

    roles = relationship(
        "Role", secondary="champions_roles", back_populates="champions"
    )
    users = relationship(
        "User", secondary="users_champions", back_populates="champions"
    )
    game = relationship("Game", back_populates="champions", uselist=False)
