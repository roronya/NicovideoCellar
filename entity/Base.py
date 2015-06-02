from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os

engine = create_engine('sqlite:///{0}/.NicovideoCrawler/db.sqlite'.format(os.environ.get('HOME')), echo=True)

Base = declarative_base()
