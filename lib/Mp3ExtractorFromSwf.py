# -*- coding: utf-8 -*-
import subprocess
import os
from SoundExtractor import SoundExtractor

class Mp3ExtractorFromSwf(SoundExtractor):
    def extract(self):
        sound_path = self._video_path + '.mp3'
        subprocess.call('swfextract -m ' + self._video_path + ' -o ' + sound_path, shell=True)
        file_handler = open(sound_path, 'rb')
        content = file_handler.read()
        file_handler.close()
        os.remove(sound_path)
        os.remove(self._video_path)
        sound = {'id': self._video['id'],
                 'content': content,
                 'type': 'mp3',
                 'title': self._video['title']}

        return sound
