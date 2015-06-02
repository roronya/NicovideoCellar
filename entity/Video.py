from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relation, backref
from Base import *

class Video(Base):
    __tablename__ = 'video'

    formal_id = Column(Integer, primary_key=True)
    id = Column(String)
    content = None
    title = None
    type = None
    mylist_id = Column(String, ForeignKey('mylist.id'))
