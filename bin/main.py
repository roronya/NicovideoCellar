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
    nicovideo_crawler = NicovideoCrawler()
    nicovideo_crawler.check_update()
