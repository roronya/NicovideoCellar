# -*- coding: utf-8 -*-

class SoundExtractor:
    _cache_path = '/tmp'
    def __init__(self, video):
        self._video = video
        self._video_path = '{0}/{1}'.format(self._cache_path, video['id'])
        file_handler = open(self._video_path, 'wb')
        file_handler.write(video['content'])
        file_handler.close()

    def extract(self):
        raise NotImplementedError()
