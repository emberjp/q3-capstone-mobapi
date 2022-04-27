from dataclasses import dataclass

from app.configs.database import db
from sqlalchemy import Column, ForeignKey, Integer, String


@dataclass
class TeamUser(db.Model):
    id: int
    funcion: str

    __tablename__ = "teams_users"

    id = Column(Integer(20), primary_key=True)
    function = Column(String)

    team_id = Column(Integer, ForeignKey("teams.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
