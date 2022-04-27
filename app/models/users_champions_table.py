from app.configs.database import db

users_champions = db.Table(
    "users_champions",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("champion_id", db.Integer, db.ForeignKey("champions.id")),
)
