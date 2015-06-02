import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../entity')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../lib')
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../repository')

from MyListRepository import MyListRepository
from ExNicovideoAPI import ExNicovideoAPI
from NicovideoCrawler import NicovideoCrawler
from ConfigReader import ConfigReader

if __name__ == '__main__':
    config = ConfigReader().read()
    mylist_repository = MyListRepository()
    ex_nicovideo_api = ExNicovideoAPI(config['mail'], config['password'])
    nicovideo_crawler = NicovideoCrawler(mylist_repository, ex_nicovideo_api)
    nicovideo_crawler.register('3291521')
