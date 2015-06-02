from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, backref
from Base import *

class Video(Base):
    __tablename__ = 'video'

    id = Column(String, primary_key = True)
    mylist_id = Column(String, ForeignKey('mylist.id'))
