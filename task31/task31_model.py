from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://python_code@localhost:5432/my_cv"
db.init_app(app)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    f_name = db.Column(db.String, nullable=False)
    l_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String)
    age = db.Column(db.Integer, nullable=False)
    last_work = db.Column(db.String, nullable=False)
    hard_skills = db.Column(db.String, nullable=False)
    soft_skills = db.Column(db.String, nullable=False)
    salary_expectations = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()
