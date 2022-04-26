from sqlalchemy import Column, ForeignKey, Integer, Table

users_positions = Table(
    "users_positions",
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("position_id", Integer, ForeignKey("positions.id")),
)
