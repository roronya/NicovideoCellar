from NicovideoAPI import NicovideoAPI
from SoundExtractorFactory import SoundExtractorFactory

class MyNicovideoAPI(NicovideoAPI):
    def __init__(self, mailaddress, password):
        super().__init__(mailaddress, password)
        self._soundExtractorFactory = SoundExtractorFactory()

    def get_video(self, video_id):
        thumb_info = self.get_thumb_info(video_id)
        video = self.get_flv(video_id)

        return {'video': video, 'type': thumb_info['movie_type'], 'id': video_id}
        
    def get_sound(self, video_id):
        video = self.get_video(video_id)
        sound_extractor = self._soundExtractorFactory.create(video)
        sound = sound_extractor.extract()

        return sound
