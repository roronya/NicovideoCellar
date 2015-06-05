from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

engine = create_engine('sqlite:///{0}/../../db.sqlite'.format(os.path.abspath(os.path.dirname(__file__))))
Base = declarative_base()
