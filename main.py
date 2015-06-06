# -*- coding: utf-8 -*-
import sys
from NicovideoCellar import NicovideoCellar

if __name__ == '__main__':
    nicovideo_cellar = NicovideoCellar('./config.json')
    if sys.argv[1] == 'update':
        nicovideo_cellar.update()
    elif sys.argv[1] == 'register':
        nicovideo_cellar.register(sys.argv[2])
