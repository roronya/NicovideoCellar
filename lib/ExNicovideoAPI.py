from NicovideoAPI import NicovideoAPI

class ExNicovideoAPI(NicovideoAPI):
    def __init__(self, mailaddress, password):
        super().__init__(mailaddress, password)

    def get_video(self, video_id):
        thumb_info = self.get_thumb_info(video_id)
        content = self.get_flv(video_id)
        video = {'content': content,
                 'type': thumb_info['movie_type'],
                 'id': video_id,
                 'title': thumb_info['title']}

        return video
