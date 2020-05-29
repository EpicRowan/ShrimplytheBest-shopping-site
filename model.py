from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Model Definitions

class User(db.model):

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement = True, primarykey=True)
    email = db.Column(db.String(64), nullable = True)
    password = db.Column(db.String(64), nullable = True)

    def __repr__(self):
        return(f"Id: {self.user_id} email: {self.email}")

class Shrimp(db.model):

    __tablename__ = "shrimps"

    shrimp_id = db.Column(db.String(), primarykey = True)
    name = db. Column(db.String(64))
    price = db.Column(db.Integer)

    def __repr__(self):
        return(f"Id: {self.shrimps_id} Name: {self.name}")


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///carbs'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will
    # leave you in a state of being able to work with the database
    # directly.

    from server import app
    connect_to_db(app)
    print("Connected to DB.")