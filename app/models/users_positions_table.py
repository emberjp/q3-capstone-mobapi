from app.configs.database import db

users_positions = db.Table(
    "users_positions",
    db.Column("id", db.Integer, primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("position_id", db.Integer, db.ForeignKey("positions.id")),
)
