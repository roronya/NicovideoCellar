from NicovideoCellar import NicovideoCellar

if __name__ == '__main__':
    nicovideo_cellar = NicovideoCellar('./config.json')
    nicovideo_cellar.register('34089083')
    nicovideo_cellar.check_update()
