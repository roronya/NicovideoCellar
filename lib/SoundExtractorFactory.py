from Mp3ExtractorFromSwf import Mp3ExtractorFromSwf
from Mp3ExtractorFromFlv import Mp3ExtractorFromFlv
from M4aExtractorFromMp4 import M4aExtractorFromMp4

class SoundExtractorFactory:
    def create(self, video):
        if (video['type'] == 'flv'):
            return Mp3ExtractorFromFlv(video)
        elif (video['type'] == 'mp4'):
            return M4aExtractorFromMp4(video)
        elif (video['type'] == 'swf'):
            return Mp3ExtractorFromSwf(video)
