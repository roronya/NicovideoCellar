# -*- coding: utf-8 -*-
from NicovideoCellar.Utility.SoundExtractor.Extractor import Mp3ExtractorFromSwf, Mp3ExtractorFromFlv, M4aExtractorFromMp4

class SoundExtractorFactory:
    def create(self, video):
        if (video['type'] == 'flv'):
            return Mp3ExtractorFromFlv(video)
        elif (video['type'] == 'mp4'):
            return M4aExtractorFromMp4(video)
        elif (video['type'] == 'swf'):
            return Mp3ExtractorFromSwf(video)
