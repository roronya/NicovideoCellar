# -*- coding: utf-8 -*-
import os
import re
from sqlalchemy.orm import sessionmaker
from NicovideoCellar.Entity import MyList
from NicovideoCellar.Entity.Base import engine

class MyListRepository:
    def __init__(self, config):
        self._session = sessionmaker(bind=engine)()
        self._config = config

    def find(self, id):
        return self._session.query(MyList).filter(MyList.id == id).one()

    def find_all(self):
        return self._session.query(MyList).all()

    def is_exist(self, mylist_id):
        if 0 < len(self._session.query(MyList).filter(MyList.id == mylist_id).all()):
            return True
        else:
            return False

    def save(self, mylist):
        self._session.add(mylist)
        self._session.commit()
        os.makedirs('{0}/{1}/{2}'.format(self._config['directory'], mylist.creator, mylist.title))
