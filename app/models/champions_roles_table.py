from sqlalchemy import Column, ForeignKey, Integer, Table

champions_roles = Table(
    "champions_roles",
    Column("id", Integer, primary_key=True),
    Column("champion_id", Integer, ForeignKey("champions.id")),
    Column("role_id", Integer, ForeignKey("roles.id")),
)
