#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from NicovideoCellar import NicovideoCellar

if __name__ == '__main__':
    nicovideo_cellar = NicovideoCellar('./config.json')
    try:
        if sys.argv[1] == 'update':
            nicovideo_cellar.update()
        elif sys.argv[1] == 'register':
            nicovideo_cellar.register(sys.argv[2])
    except IndexError:
        print('update\t登録されたマイリストをアップデート')
        print('register :mylist_id\tマイリストIDを登録')
