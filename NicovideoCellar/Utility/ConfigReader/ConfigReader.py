# -*- coding: utf-8 -*-
import json
import sys
import os

class ConfigReader:
    def read(self, config_file_path):
        file_handler = open(config_file_path, 'r')
        config_json = file_handler.read()
        file_handler.close()
        config = json.loads(config_json)
        return config
