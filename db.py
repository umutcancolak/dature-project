from flask_sqlalchemy import SQLAlchemy
from database import Database

db = SQLAlchemy()
mongo_db = Database.initialize()
