"""Database connection module."""

import os
import configparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

config = configparser.ConfigParser()
config.read("config.ini")
mysql_config = config["mysql"]
mysql_server: str = mysql_config["SERVER"]
mysql_username: str = mysql_config["USERNAME"]
mysql_password: str = mysql_config["PASSWORD"]
mysql_database: str = mysql_config["DATABASE"]
mysql_port: str = mysql_config["PORT"]
database_uri: str = os.getenv(
    "DATABASE_URI",
    f"mysql+pymysql://{mysql_username}:{mysql_password}@{mysql_server}:{mysql_port}/{mysql_database}",
)
db = create_engine(database_uri)
Base = declarative_base()
Session = sessionmaker(bind=db)
