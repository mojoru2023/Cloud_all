

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
from lxml import etree
from selenium import webdriver




















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



class Js_future(object):
    def __init__(self,url):
        self.url = url


    def page_request(self):

        '''
        服务器上必须配置无头模式
        '''
        ch_options = webdriver.ChromeOptions()
        # 为Chrome配置无头模式
        ch_options.add_argument("--headless")
        ch_options.add_argument('--no-sandbox')
        ch_options.add_argument('--disable-gpu')
        ch_options.add_argument('--disable-dev-shm-usage')
        # 在启动浏览器时加入配置
        driver = webdriver.Chrome(options=ch_options)


        driver.get(self.url)
        html = driver.page_source
        driver.quit()
        return html

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="readArea"]/div[2]/div/table/tbody/tr[2]/td[6]/text()[1]')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(f_price[0])


class Js_spot(object):
    def __init__(self,url):
        self.url = url



    def page_request(self):

        '''
        服务器上必须配置无头模式
        '''
        ch_options = webdriver.ChromeOptions()
        # 为Chrome配置无头模式
        ch_options.add_argument("--headless")
        ch_options.add_argument('--no-sandbox')
        ch_options.add_argument('--disable-gpu')
        ch_options.add_argument('--disable-dev-shm-usage')
        # 在启动浏览器时加入配置
        driver = webdriver.Chrome(options=ch_options)


        driver.get(self.url)
        html = driver.page_source
        driver.quit()
        return html

    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''


        html  = self.page_request()
        element = etree.HTML(html)

        now_price = element.xpath(
            '//*[@id="price"]/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(f_price[1])
        print(now_price)




def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into js225_future_spot (js225_future,js225_spot,furtur_spot_spread1,furtur_spot_spread2) values (%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass






if __name__ == '__main__':
    while True:


        big_list = []
        js_future_url = 'https://port.jpx.co.jp/jpx/template/quote.cgi?F=tmp/e_popchart&QCODE=111.555/O'
        js_spot_url = 'https://indexes.nikkei.co.jp/nkave/index/profile?idx=nk225'

        js_future = Js_future(js_future_url)
        js_future.page_parse_()
        js_spot = Js_spot(js_spot_url)
        js_spot.page_parse_()
        print(big_list)

        #
        furtur_spot_spread1 = float(big_list[0])/float(big_list[1])
        furtur_spot_spread2 = float(big_list[0])-float(big_list[1])

        title_l = [big_list[0],big_list[1],furtur_spot_spread1,furtur_spot_spread2]

        ff_l = []
        f_tup = tuple(title_l)
        ff_l.append((f_tup))
        print(big_list)
        print(ff_l)
        insertDB(ff_l)
        time.sleep(60)
        print(datetime.datetime.now())
#1720
# 1803
# 3612
# 4555




# create table js225_future_spot(id int not null primary key auto_increment,js225_future FLOAT,js225_spot FLOAT,furtur_spot_spread1 FLOAT,furtur_spot_spread2 FLOAT,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;




