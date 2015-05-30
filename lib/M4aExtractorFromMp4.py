# -*- coding: utf-8 -*-
import subprocess
from SoundExtractor import SoundExtractor

class M4aExtractorFromMp4(SoundExtractor):
    def extract(self):
        sound_path = self._video_path + '.m4a'
        subprocess.call('ffmpeg -i ' + self._video_path + ' -vn -acodec copy ' + sound_path, shell=True)
        file_handler = open(sound_path, 'rb')
        content = file_handler.read()
        file_handler.close()
        sound = {'id': self._video['id'],
                 'content': content,
                 'type': 'm4a',
                 'title': self._video['title']}

        return sound
