import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../entity')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../lib')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../repository')

from MyList import MyList
from MyListRepository import MyListRepository
from ExNicovideoAPI import ExNicovideoAPI
from ConfigReader import ConfigReader

class NicovideoCrawler:
    def __init__(self):
        config = ConfigReader().read()
        self._mylist_repository = MyListRepository()
        self._ex_nicovideo_api = ExNicovideoAPI(config['mail'], config['password'])

    def register(self, mylist_id):
        if not self._mylist_repository.is_exist(mylist_id):
            mylist_info = self._ex_nicovideo_api.get_mylist_info(mylist_id)
            mylist = MyList(id=mylist_info['id'], title=mylist_info['title'], creator=mylist_info['creator'])
            self._mylist_repository.save(mylist)
