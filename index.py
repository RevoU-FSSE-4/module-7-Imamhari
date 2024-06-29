from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from models.user import User

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():

    # Insert data using SQLALchemy
    NewUser = User(username="aziz", email="aziz313@gmail.com", password="1234", role="user")
    Session = sessionmaker(connection)
    with Session() as session:
        session.add(NewUser)
        session.commit()

    return "Inserted Successfully!"

if __name__ == "__main__":
    app.run(debug=True)