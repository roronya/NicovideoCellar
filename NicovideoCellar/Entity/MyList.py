from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from NicovideoCellar.Entity.Base import *
from NicovideoCellar.Entity.Video import Video

class MyList(Base):
    __tablename__ = 'mylist'

    id = Column(String, primary_key = True)
    title = Column(String(255))
    creator = Column(String(255))
    videos = relationship('Video', backref='mylist')
