# coding:utf-8

from bs4 import BeautifulSoup
from urlparse import urljoin
import requests
import csv

url = 'http://bj.58.com/pinpaigongyu/pn/{page}/?minprice=2000_3000'

# 已完成的页数序号，初始为0
page = 0

# 打开csv文件
csv_file = open('rent.csv', 'wb')
# 创建write对象，指定文件与分隔符
csv_write = csv.writer(csv_file, delimiter=',')

while True:
    page += 1
    print('fetch: ', url.format(page=page))
    # 获取目标页面
    response = requests.get(url.format(page=page))
    # 获取页面正文，创建一个Beautiful对象
    html = BeautifulSoup(response.text)
    # 获取class=page的元素下的所有a元素
    house_list = html.select('.list > li')

    # 循环在读不到新的房源时结束
    if not house_list:
        break

    for house in house_list:
        # 得到标签包裹着的文本
        house_title = house.select('h2')[0].string.encode('utf8')
        # 得到标签内属性值；由于读取到的链接路径是相对路径，所以需要urljoin得到完整的url地址
        house_url = urljoin(url, house.select('a')[0]['href'])
        house_info_list = house_title.split()

        # 如果第二列是公寓名则取第一列作为地址
        if '公寓' in house_info_list[1] or '青年社区' in house_info_list[1]:
            house_location = house_info_list[0]
        else:
            house_location = house_info_list[1]

        house_money = house.select('.money')[0].select('b')[0].string.encode('utf8')
        # 写一行数据
        csv_write.writerow([house_title, house_location, house_money, house_url])

# 关闭文件
csv_file.close()
