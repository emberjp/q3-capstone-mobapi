from app.configs.database import db

champions_roles = db.Table(
    "champions_roles",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("champion_id", db.Integer, db.ForeignKey("champions.id")),
    db.Column("role_id", db.Integer, db.ForeignKey("roles.id")),
)
