

from l_p_config import *
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

def retry_if_io_error(exception):
    return isinstance(exception, ZeroDivisionError)







def run_forever(func):
    def wrapper(obj):
        while True:
            func(obj)
    return wrapper


def RemoveDot(item):
    f_l = []
    for it in item:

        f_str = "".join(it.split(","))
        ff_str = f_str +"00"
        f_l.append(ff_str)

    return f_l

def remove_douhao(num):
    num1 = "".join(num.split(","))
    f_num = str(num1)
    return f_num
def remove_block(items):
    new_items = []
    for it in items:
        f = "".join(it.split())
        new_items.append(f)
    return new_items
def call_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


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
        big_list.append(float(f_price[0]))
        print(f_price[0])
        return big_list









def get_index():
    index_code = ["0000", "0040"]
    for i_code in index_code:
        url ='https://kabutan.jp/stock/?code={0}'.format(i_code)
        html =call_page(url)
        element = etree.HTML(html)

        now_price = element.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
        f_price = RemoveDot(remove_block(now_price))
        big_list.append(float(f_price[0]))




if __name__ == "__main__":
    s = datetime.datetime.now()

    big_list = []
    f_compare_content = []
    get_index()
    data_list = [d_2021_10_23, d_2021_11_16, d_2021_12_28, d_2022_1_22]
    for item1, item2 in zip(data_list, month_dbname):

        for it in js225_400_codes:

            url = "https://minkabu.jp/stock/{0}".format(it)
            print(url)
            jsp = JSPool_M(url)# 这里把请求和解析都进行了处理
            jsp.page_parse_()
        ff_l = []

        print(len(item1[2:]))
        print(len(big_list[2:]))
        index225_ = (big_list[0] - item1[0]) / item1[0]
        index400_ = (big_list[1] - item1[1]) / item1[1]

        f_compare_content.append(str(round(index225_,5)))
        f_compare_content.append(str(round(index400_,5)))

        for i1,i2 in zip(big_list[2:],item1[2:]):
            f_compare_content.append(round(((i1 - i2) / i2), 5))


        f_tup = tuple(f_compare_content)
        print(f_tup)
        ff_l.append((f_tup))
        print(ff_l)
        print(big_list)
        print(f_compare_content)
        connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS',
                                     charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

        cursor = connection.cursor()

        try:
            # 用一个列表解析
            f_jsp = ["J" + cod for cod in into_db]
            sp_func = lambda x: ",".join(x)
            f_lcode = sp_func(f_jsp)

            f_ls = "%s," * len(into_db)
            fc = f_lcode
            print(len(fc.split(",")))
            print(len(f_ls[:-1].split(",")))
            cursor.executemany('insert into {2} ({0}) values ({1})'.format(fc, f_ls[:-1],item2), ff_l)
            connection.commit()
            connection.commit()
            connection.close()
            print('向MySQL中添加数据成功！')
        except TypeError:
            pass
        e = datetime.datetime.now()
        print(e-s)





















 #   create table js225_400_leverage_2021_1116(id int not null primary key auto_increment,J225 float,J400 float,J1332 float, J1333 float, J1417 float, J1605 float, J1719 float, J1720 float, J1721 float, J1766 float, J1801 float, J1802 float, J1803 float, J1808 float, J1812 float, J1820 float, J1821 float, J1824 float, J1860 float, J1861 float, J1878 float, J1881 float, J1893 float, J1911 float, J1925 float, J1928 float, J1942 float, J1951 float, J1959 float, J1963 float, J1973 float, J2002 float, J2121 float, J2127 float, J2146 float, J2175 float, J2181 float, J2201 float, J2229 float, J2264 float, J2267 float, J2269 float, J2281 float, J2282 float, J2317 float, J2327 float, J2331 float, J2337 float, J2371 float, J2379 float, J2412 float, J2413 float, J2427 float, J2432 float, J2433 float, J2501 float, J2502 float, J2503 float, J2531 float, J2587 float, J2593 float, J2651 float, J2670 float, J2702 float, J2768 float, J2782 float, J2784 float, J2801 float, J2802 float, J2809 float, J2811 float, J2815 float, J2871 float, J2875 float, J2897 float, J2914 float, J3003 float, J3038 float, J3048 float, J3064 float, J3086 float, J3088 float, J3092 float, J3099 float, J3101 float, J3103 float, J3107 float, J3116 float, J3141 float, J3148 float, J3167 float, J3231 float, J3244 float, J3254 float, J3288 float, J3289 float, J3291 float, J3349 float, J3360 float, J3382 float, J3391 float, J3401 float, J3402 float, J3405 float, J3407 float, J3436 float, J3543 float, J3549 float, J3563 float, J3626 float, J3635 float, J3659 float, J3738 float, J3765 float, J3769 float, J3861 float, J3863 float, J3880 float, J3923 float, J3932 float, J3941 float, J4004 float, J4005 float, J4021 float, J4042 float, J4043 float, J4061 float, J4063 float, J4088 float, J4091 float, J4151 float, J4182 float, J4183 float, J4188 float, J4202 float, J4204 float, J4205 float, J4206 float, J4208 float, J4307 float, J4324 float, J4348 float, J4403 float, J4452 float, J4502 float, J4503 float, J4506 float, J4507 float, J4516 float, J4519 float, J4521 float, J4523 float, J4527 float, J4528 float, J4536 float, J4543 float, J4552 float, J4553 float, J4568 float, J4578 float, J4587 float, J4612 float, J4613 float, J4631 float, J4661 float, J4684 float, J4686 float, J4689 float, J4704 float, J4716 float, J4732 float, J4739 float, J4751 float, J4755 float, J4768 float, J4812 float, J4816 float, J4819 float, J4848 float, J4849 float, J4887 float, J4901 float, J4902 float, J4911 float, J4912 float, J4921 float, J4922 float, J4927 float, J4967 float, J5019 float, J5020 float, J5021 float, J5101 float, J5105 float, J5108 float, J5110 float, J5201 float, J5202 float, J5214 float, J5232 float, J5233 float, J5301 float, J5332 float, J5333 float, J5334 float, J5393 float, J5401 float, J5406 float, J5411 float, J5541 float, J5631 float, J5703 float, J5706 float, J5707 float, J5711 float, J5713 float, J5714 float, J5801 float, J5802 float, J5803 float, J5857 float, J5929 float, J5947 float, J6005 float, J6028 float, J6035 float, J6055 float, J6098 float, J6103 float, J6113 float, J6134 float, J6136 float, J6141 float, J6146 float, J6178 float, J6183 float, J6201 float, J6235 float, J6268 float, J6273 float, J6301 float, J6302 float, J6305 float, J6326 float, J6361 float, J6367 float, J6383 float, J6432 float, J6448 float, J6465 float, J6471 float, J6472 float, J6473 float, J6479 float, J6501 float, J6503 float, J6504 float, J6506 float, J6532 float, J6544 float, J6586 float, J6594 float, J6645 float, J6670 float, J6674 float, J6701 float, J6702 float, J6703 float, J6723 float, J6724 float, J6727 float, J6728 float, J6750 float, J6752 float, J6753 float, J6754 float, J6758 float, J6762 float, J6770 float, J6841 float, J6845 float, J6849 float, J6856 float, J6857 float, J6861 float, J6869 float, J6902 float, J6920 float, J6923 float, J6952 float, J6954 float, J6965 float, J6971 float, J6976 float, J6981 float, J6988 float, J7003 float, J7004 float, J7011 float, J7012 float, J7013 float, J7148 float, J7164 float, J7167 float, J7177 float, J7186 float, J7201 float, J7202 float, J7203 float, J7205 float, J7211 float, J7259 float, J7261 float, J7267 float, J7269 float, J7270 float, J7272 float, J7276 float, J7282 float, J7309 float, J7313 float, J7419 float, J7453 float, J7459 float, J7516 float, J7532 float, J7550 float, J7564 float, J7575 float, J7649 float, J7701 float, J7717 float, J7729 float, J7731 float, J7733 float, J7735 float, J7741 float, J7747 float, J7751 float, J7752 float, J7762 float, J7832 float, J7846 float, J7911 float, J7912 float, J7947 float, J7951 float, J7956 float, J7974 float, J7988 float, J8001 float, J8002 float, J8015 float, J8020 float, J8031 float, J8035 float, J8053 float, J8056 float, J8058 float, J8088 float, J8111 float, J8113 float, J8194 float, J8233 float, J8252 float, J8253 float, J8267 float, J8273 float, J8279 float, J8282 float, J8283 float, J8303 float, J8304 float, J8306 float, J8308 float, J8309 float, J8316 float, J8331 float, J8354 float, J8355 float, J8410 float, J8411 float, J8424 float, J8425 float, J8439 float, J8473 float, J8570 float, J8572 float, J8585 float, J8591 float, J8593 float, J8595 float, J8601 float, J8604 float, J8628 float, J8630 float, J8697 float, J8725 float, J8750 float, J8766 float, J8795 float, J8801 float, J8802 float, J8804 float, J8830 float, J8850 float, J8876 float, J8892 float, J8905 float, J8919 float, J9001 float, J9005 float, J9007 float, J9008 float, J9009 float, J9020 float, J9021 float, J9022 float, J9042 float, J9062 float, J9064 float, J9065 float, J9069 float, J9086 float, J9090 float, J9101 float, J9104 float, J9107 float, J9142 float, J9143 float, J9202 float, J9301 float, J9375 float, J9418 float, J9432 float, J9433 float, J9434 float, J9435 float, J9501 float, J9502 float, J9503 float, J9504 float, J9506 float, J9508 float, J9509 float, J9513 float, J9517 float, J9519 float, J9531 float, J9532 float, J9602 float, J9613 float, J9627 float, J9678 float, J9684 float, J9697 float, J9719 float, J9735 float, J9744 float, J9766 float, J9787 float, J9810 float, J9843 float, J9962 float, J9983 float, J9984 float, J9989 float,LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;




