from NicovideoAPI import NicovideoAPI

class MyNicovideoAPI(NicovideoAPI):
    def __init__(self, mailaddress, password):
        super().__init__(mailaddress, password)
        _soundExtractor = SoundExtractor()

    def get_video(self, video_id):
        thumb_info = self.get_thumb_info(video_id)
        video = self.get_flv(video_id)

        return {'video': video, 'type': thumb_info['movie_type'], 'id': video_id}
