# coding:utf8

# from bs4 import BeautifulSoup
import requests
import json

# Post请求封装
url = 'http://www.mafengwo.cn/search/s.php'
data = {
    "q": "Tokyo",
    "seid": "2D390BC2-AF43-4613-A645-81524FC5EB23"
}


def send_post(url,data):
    res = requests.get(url=url, data=data)
    return res.text
print send_post(url, data)





