import os
import re
from NicovideoCellar.Utility.ConfigReader.ConfigReader import ConfigReader
from sqlalchemy.orm import sessionmaker
from NicovideoCellar.Entity.Base import *
from NicovideoCellar.Entity.Video import Video

class VideoRepository:
    def __init__(self):
        self._session = sessionmaker(bind=engine)()
        self._config = ConfigReader().read(os.path.abspath(os.path.dirname(__file__)) + '/../../config.json')

    def save(self, video):
        self._session.add(video)
        self._session.commit()
        file_handler = open('{0}/{1}/{2}/{3}.{4}'.format(self._config['directory'], video.mylist.creator, video.mylist.title, re.sub(r'/', '／', video.title), video.type), 'wb')
        file_handler.write(video.content)
        file_handler.close()
