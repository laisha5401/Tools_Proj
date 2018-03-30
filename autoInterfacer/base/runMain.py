# coding:utf8

import requests
import json


class RunMain():

    def __init__(self, url, s, data):
        pass

    def send_get(self, url, data):
        res = requests.get(url=url, data=data).json()
        return res

    def send_post(self, url, data):
        res = requests.post(url=url, data=data).json()
        return res

    def run_main(self, url, method, data=None):
        res= None
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)
        return res


if __name__ == '__main__':
    url = 'http://www.mafengwo.cn/search/s.php'
    data = {
        'q': "Tokyo",
        'seid': '2D390BC2-AF43-4613-A645-81524FC5EB23'
    }
    run = RunMain(url, 'GET', data)
    print run.res
