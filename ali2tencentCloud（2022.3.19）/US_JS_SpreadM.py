
import datetime
import time

import pymysql
import requests
from lxml import etree
import json
from queue import Queue
import threading
from requests.exceptions import RequestException




from retrying import retry
import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException

def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

# 正则和lxml混用
def parse_html(html):  # 正则专门有反爬虫的布局设置，不适合爬取表格化数据！



    selector = etree.HTML(html)
    Price = selector.xpath('//*[@id="spFP"]/div[1]/span[1]/text()')
    for item in Price:
        big_list.append(item)








def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        f_l.append(f_str)

    return f_l




def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)






'''
1. 创建 URL队列, 响应队列, 数据队列 在init方法中
2. 在生成URL列表中方法中,把URL添加URL队列中
3. 在请求页面的方法中,从URL队列中取出URL执行,把获取到的响应数据添加响应队列中
4. 在处理数据的方法中,从响应队列中取出页面内容进行解析, 把解析结果存储数据队列中
5. 在保存数据的方法中, 从数据队列中取出数据,进行保存
6. 开启几个线程来执行上面的方法
'''

def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper




def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num



class JSPool_M(object):

    def __init__(self,url):
        self.url = url

    def page_request(self):
        ''' 发送请求获取数据 '''
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

        response = requests.get(self.url,headers=headers)
        if response.status_code == 200:
            html = response.text
            return html
        else:
            pass

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="layout"]/div[2]/div[3]/div[2]/div/div[1]/div/div/div[1]/div[2]/div/div[2]/div/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(f_price[0])
        return big_list






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into us_js_SM (js_225_400,js225_sp500,js225_nas100,nas100_sp500,js400_sp500,js400_nas100) values (%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






if __name__ == '__main__':
    big_list = []
    js225_url ='https://minkabu.jp/stock/100000018'
    js400_url ='https://minkabu.jp/stock/KSISU102B'




    jsp1 = JSPool_M(js225_url)# 这里把请求和解析都进行了处理
    jsp1.page_parse_()
    jsp2 = JSPool_M(js400_url)# 这里把请求和解析都进行了处理
    jsp2.page_parse_()

    sp500_url = 'https://gu.qq.com/usINX/zs'
    nas_100 = 'https://gu.qq.com/usIXIC/zs'



    us_l =[sp500_url,nas_100]
    for item in us_l:

        html_ = call_page(item)
        parse_html(html_)

    js225_=big_list[0]
    js400_=big_list[1]
    sp500_=big_list[2]
    nas_100_=big_list[3]
    # 要价差，不要比价
    js_225_400 = float(js225_)-float(js400_)
    js225_sp500 =  float(js225_)-float(sp500_)
    js225_nas100 = float(js225_)-float(nas_100_)
    nas100_sp500 = float(nas_100_)-float(sp500_)
    js400_sp500 =  float(js400_)-float(sp500_)
    js400_nas100 = float(js400_)-float(nas_100_)
    title_l = [js_225_400,js225_sp500,js225_nas100,nas100_sp500,js400_sp500,js400_nas100]

    ff_l = []
    f_tup = tuple(title_l)
    ff_l.append((f_tup))
    print(big_list)
    print(ff_l)
    insertDB(ff_l)
