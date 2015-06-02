from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from Base import *
from Video import Video

class MyList(Base):
    __tablename__ = 'mylist'

    id = Column(String, primary_key = True)
    videos = relationship('Video', backref='mylist')
