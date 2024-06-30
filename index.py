from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from models.user import User

from controllers.user import user_routes
from controllers.data_review import data_review_routes
import os

from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(user_routes)
app.register_blueprint(data_review_routes)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    Session = sessionmaker(connection)
    s = Session()
    return s.query(User).get(int(user_id))



@app.route("/")
def index():

    # Insert data using SQLALchemy
    NewUser = User(username="tomura", email="tomura13@gmail.com", password="1234", role="")
    Session = sessionmaker(connection)
    with Session() as session:
        session.add(NewUser)
        session.commit()

    return "Inserted Successfully!"

if __name__ == "__main__":
    app.run(debug=True)