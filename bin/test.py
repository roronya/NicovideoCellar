import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../src')

from ConfigReader.ConfigReader import ConfigReader
from Repository.MyListRepository import MyListRepository
from NicovideoCrawler.NicovideoCrawler import NicovideoCrawler

print(ConfigReader().read(os.path.abspath(os.path.dirname(__file__)) + '/../config.json'))
mylist_repository = MyListRepository()
print(mylist_repository.find_all())
crawler = NicovideoCrawler()
crawler.check_update()
