import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../entity')

from sqlalchemy.orm import sessionmaker
from Base import *
from MyList import MyList

class MyListRepository:
    def __init__(self):
        self._session = sessionmaker(bind=engine)()

    def find(self, id):
        return self._session.query(MyList).filter(MyList.id == id).one()

    def is_exist(self, mylist_id):
        if 0 < len(self._session.query(MyList).filter(MyList.id == mylist_id).all()):
            return True
        else:
            return False

    def save(self, mylist):
        self._session.add(mylist)
        self._session.commmit()
