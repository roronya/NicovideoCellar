import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../src')

from NicovideoCrawler.NicovideoCrawler import NicovideoCrawler

if __name__ == '__main__':
    nicovideo_crawler = NicovideoCrawler()
    nicovideo_crawler.register('34089083')
    nicovideo_crawler.check_update()
