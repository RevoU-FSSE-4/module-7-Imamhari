from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():

    Session = sessionmaker(connection)
    with Session() as session:
        session.execute(text("INSERT INTO user (username, email, password, role) VALUES('imamhm', 'f7hJ9@example.com', '12345', 'admin')"))
        session.commit()

    return "Inserted Successfully!"

if __name__ == "__main__":
    app.run(debug=True)