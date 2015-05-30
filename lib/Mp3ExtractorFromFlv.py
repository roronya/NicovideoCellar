# -*- coding: utf-8 -*-
import subprocess
from SoundExtractor import SoundExtractor

class Mp3ExtractorFromFlv(SoundExtractor):
    def extract(self):
        sound_path = self._video_path + '.mp3'
        subprocess.call('ffmpeg -i ' + self._video_path + ' -acodec copy ' + sound_path, shell=True)
        file_handler = open(sound_path, 'rb')
        content = file_handler.read()
        file_handler.close()
        sound = {'id': self._video['id'],
                 'content': content,
                 'type': 'mp3',
                 'title': self._video['title']}
                 
        return sound
