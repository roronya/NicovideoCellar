import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/..')

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref

from Entity.Base import *
from Entity.Video import Video

class MyList(Base):
    __tablename__ = 'mylist'

    id = Column(String, primary_key = True)
    title = Column(String(255))
    creator = Column(String(255))
    videos = relationship('Video', backref='mylist')
