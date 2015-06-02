# -*- coding: utf-8 -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)) + '/../entity')

from Base import *
from Video import Video
from MyList import MyList

Base.metadata.create_all(engine)
