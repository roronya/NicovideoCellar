# -*- coding: utf-8 -*-
import requests
from pyquery import PyQuery as pq
import re

from NicovideoCellar.Utility.NicovideoAPI.NicovideoAPI import NicovideoAPI
from NicovideoCellar.Utility.SoundExtractor.SoundExtractorFactory import SoundExtractorFactory

class ExNicovideoAPI(NicovideoAPI):
    def __init__(self, mailaddress, password):
        super().__init__(mailaddress, password)
        self._soundExtractorFactory = SoundExtractorFactory()

    def get_video(self, video_id):
        thumb_info = self.get_thumb_info(video_id)
        content = self.get_flv(video_id)
        video = {'content': content,
                 'type': thumb_info['movie_type'],
                 'id': video_id,
                 'title': thumb_info['title']}
        return video

    def get_sound(self, video_id):
        video = self.get_video(video_id)
        sound_extractor = self._soundExtractorFactory.create(video)
        sound = sound_extractor.extract()
        return sound

    def get_video_ids_from_mylist(self, mylist_id):
        mylist_xml = requests.get('http://www.nicovideo.jp/mylist/{0}?rss=2.0&lkang=ja-jp'.format(mylist_id))
        dom = pq(mylist_xml.content, parser='xml')
        return [re.search(r'[^/]*$', link.text).group(0) for link in dom('channel item link')]

    def get_mylist_info(self, mylist_id):
        mylist_xml = requests.get('http://www.nicovideo.jp/mylist/{0}?rss=2.0&lkang=ja-jp'.format(mylist_id))
        dom = pq(mylist_xml.content, parser='xml')
        title = dom('channel > title').text()
        creator = dom('channel > dc\:creator').text()
        mylist = {'id': mylist_id,
                  'title': title,
                  'creator': creator}
        return mylist
