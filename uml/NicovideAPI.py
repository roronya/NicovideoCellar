# -*- coding: utf-8 -*-
import requests
import urllib.parse
import re

class NicovideoAPI:
    def __init__(self, mailaddress, password):
        self.login(mailaddress, password)

    def login(self, mailaddress, password):
        response = requests.post(
            "https://secure.nicovideo.jp/secure/login?site=niconico",
            data = {'mail_tel': mailaddress,
                    'password': password},
            allow_redirects = False
        )
        self._cookies = response.cookies
        
    def get_flv(self, movie_id):
        flv_url = self._get_flv_url(movie_id)
        self._cookies.update(self._get_nicohistory_cookie(movie_id))
        response = requests.get(flv_url, cookies=self._cookies)
        flv = response.content

        return flv

    def _get_flv_url(self, movie_id):
        response = requests.get('http://flapi.nicovideo.jp/api/getflv/' + movie_id, cookies=self._cookies)
        response_body = urllib.parse.unquote(response.text)
        flv_url = re.search(r'url=([^&]+)', response_body).group(1)
        
        return flv_url

    def _get_nicohistory_cookie(self, movie_id):
        response = requests.get('http://www.nicovideo.jp/watch/' + movie_id, cookies=self._cookies)

        return response.cookies
