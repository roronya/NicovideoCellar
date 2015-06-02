import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/..')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, backref
from Entity.Base import *

class Video(Base):
    __tablename__ = 'video'

    formal_id = Column(Integer, primary_key=True)
    id = Column(String)
    content = None
    title = None
    type = None
    mylist_id = Column(String, ForeignKey('mylist.id'))
