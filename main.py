from NicovideoCrawler import NicovideoCrawler

if __name__ == '__main__':
    nicovideo_crawler = NicovideoCrawler('./config.json')
    nicovideo_crawler.register('34089083')
    nicovideo_crawler.check_update()
