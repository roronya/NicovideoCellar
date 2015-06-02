# -*- coding: utf-8 -*-
import os
import sys

class SoundExtractor:
    _path = os.path.abspath(os.path.dirname(__file__)) + '/../cache'
    def __init__(self, video):
        self._video = video
        self._video_path = '{0}/{1}'.format(self._path, video['id'])
        file_handler = open(self._video_path, 'wb')
        file_handler.write(video['content'])
        file_handler.close()

    def extract(self):
        raise NotImplementedError()
