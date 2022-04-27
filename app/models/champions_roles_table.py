# from sqlalchemy import Column, ForeignKey, Integer, Table

# champions_roles = Table(
#     "champions_roles",
#     Column("id", Integer, primary_key=True),
#     Column("champion_id", Integer, ForeignKey("champions.id")),
#     Column("role_id", Integer, ForeignKey("roles.id")),
# )

from app.configs.database import db

champions_roles = db.Table(
    "champions_roles",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("champion_id", db.Integer, db.ForeignKey("champions.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id")),
)
