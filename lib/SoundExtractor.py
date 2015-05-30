# -*- coding: utf-8 -*-

class SoundExtractor:
    _path = '/tmp/'
    def __init__(self, video):
        self._video = video
        self._video_path = self._path + video['id']
        file_handler = open(self._video_path, 'wb')
        file_handler.write(video['content'])
        file_handler.close()

    def extract(self):
        raise NotImplementedError()
