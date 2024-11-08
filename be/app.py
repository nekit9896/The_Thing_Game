from flask import Flask
from be.table_models import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
