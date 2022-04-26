from sqlalchemy import Column, ForeignKey, Integer, Table

users_champions = Table(
    "users_champions",
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("champion_id", Integer, ForeignKey("champions.id")),
)
