from sqlalchemy import create_engine
import os

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
database = os.getenv("DB_DATABASE")

print("Connecting to MySQL database...")

engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}/{database}")
connection = engine.connect()
print("Connected to MySQL database!")