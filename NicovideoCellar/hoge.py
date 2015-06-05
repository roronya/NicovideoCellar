# -*- coding: utf-8 -*-
from NicovideoCellar.Entity import MyList, Video
from NicovideoCellar.Utility import ExNicovideoAPI, SoundExtractorFactory, ConfigReader
from NivocideoCellar.Repository import MyListRepository, VideoRepository

class NicovideoCellar:
    def __init__(self, config_path):
        self._config = ConfigReader().read(config_path)
        self._mylist_repository = MyListRepository()
        self._video_repository = VideoRepository()
        self._ex_nicovideo_api = ExNicovideoAPI(self._config['mail'], self._config['password'])

    def register(self, mylist_id, title=None, creator=None):
        if not self._mylist_repository.is_exist(mylist_id):
            mylist_info = self._ex_nicovideo_api.get_mylist_info(mylist_id)
            if title is None:
                title = mylist_info['title']
            if creator is None:
                creator = mylist_info['creator']
            mylist = MyList(id=mylist_id, title=title, creator=creator)
            self._mylist_repository.save(mylist)

    def check_update(self):
        registered_mylists = self._mylist_repository.find_all()
        for mylist in registered_mylists:
            unregistered_video_ids = self._get_unregistered_video_ids(mylist)
            for video_id in unregistered_video_ids:
                sound = self._ex_nicovideo_api.get_sound(video_id)
                video = Video(id=video_id, content=sound['content'], title=sound['title'], type=sound['type'], mylist_id=mylist.id)
                self._video_repository.save(video)

    def _get_unregistered_video_ids(self, mylist):
        registered_video_ids = set([video.id for video in mylist.videos])
        upload_video_ids =  set(self._ex_nicovideo_api.get_video_ids_from_mylist(mylist.id))
        unregistered_video_ids = upload_video_ids - registered_video_ids
        return unregistered_video_ids
