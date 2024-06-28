from flask import Flask
from dotenv import load_dotenv
from connectors.mysql_connector import connection

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"