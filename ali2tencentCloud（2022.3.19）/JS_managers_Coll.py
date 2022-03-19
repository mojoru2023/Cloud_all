import os

import pymysql
import csv
import csv
import datetime
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


from selenium.common.exceptions import WebDriverException

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

import os
import re
import time
import sys
type = sys.getfilesystemencoding()
import pymysql
import xlrd
import requests
from requests.exceptions import RequestException
from lxml import etree
# 数据处理好，看如何塞入execl中

# 读取code---形成fm----筛选股票池----定池子----跟踪模型与模板




def retry_if_io_error(exception):
    print("---------------------------")
    return isinstance(exception, WebDriverException)



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
    return isinstance(exception, WebDriverException)
def retry_if_io_error1(exception):
    return isinstance(exception, IndexError)
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
    num1 = num[0].split("円")[0].split(",")
    f_num = "".join(num1)
    return f_num



class JSPool_M1(object):

    def __init__(self, url):
        self.url = url




    def page_parse_(self):
        '''根据页面内容使用lxml解析数据, 获取段子列表'''

        html = requests.get(self.url)
        element = etree.HTML(html.text)

        now_price = element.xpath('//*[@id="stockinfo_i1"]/div[2]/span[2]/text()')
        industry = element.xpath('//*[@id="stockinfo_i2"]/div/a/text()')
        bonus = element.xpath('//*[@id="finance_box"]/div[5]/table/tbody/tr[6]/td[6]/text()')
        name = element.xpath('//*[@id="stockinfo_i1"]/div[1]/h2/text()')
        return now_price[0],industry[0],bonus[0],name[0]



class JSPool_M2(object):

    def __init__(self, url):
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

        html = self.page_request()
        element = etree.HTML(html)


        manager = element.xpath('//*[@id="pro_body"]/center/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[8]/td[2]/text()')
        f_manager = remove_block(manager)
        setuptime = element.xpath('//*[@id="pro_body"]/center/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[9]/td[2]/text()')
        listingtime = element.xpath('//*[@id="pro_body"]/center/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[11]/td[2]/text()')
        settleday = element.xpath('//*[@id="pro_body"]/center/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[12]/td[2]/text()')
        employees = element.xpath('//*[@id="pro_body"]/center/div[5]/div[1]/div[2]/table/tbody/tr[1]/td/table/tbody/tr[14]/td[2]/text()')
        return f_manager[0],setuptime[0],listingtime[0],settleday[0],employees[0]


def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        cursor.executemany('insert into JS_manager (code,now_price,industry,bonus,name,manager,setuptime,listingtime,settleday,employee) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError:
        pass

def csv_dict_write(path,head,data):
    with open(path,'w',encoding='utf-8',newline='') as f:
        writer = csv.DictWriter(f,head)
        writer.writeheader()
        writer.writerows(data)
        return True
def read_xlrd(excelFile):
    data = xlrd.open_workbook(excelFile)
    table = data.sheet_by_index(0)
    dataFile = []
    for rowNum in range(table.nrows):
        dataFile.append(table.row_values(rowNum))

       # # if 去掉表头
       # if rowNum > 0:

    return dataFile






if __name__ =='__main__':
    # js225_400_codes = ['1332', '1333', '1417', '1605', '1719', '1720', '1721', '1766', '1801', '1802', '1803', '1808',
    #                    '1812', '1820', '1821', '1824', '1860', '1861', '1878', '1881', '1893', '1911', '1925', '1928',
    #                    '1942', '1951', '1959', '1963', '1973', '2002', '2121', '2127', '2146', '2175', '2181', '2201',
    #                    '2229', '2264', '2267', '2269', '2281', '2282', '2317', '2327', '2331', '2337', '2371', '2379',
    #                    '2412', '2413', '2427', '2432', '2433', '2501', '2502', '2503', '2531', '2587', '2593', '2651',
    #                    '2670', '2702', '2768', '2782', '2784', '2801', '2802', '2809', '2811', '2815', '2871', '2875',
    #                    '2897', '2914', '3003', '3038', '3048', '3064', '3086', '3088', '3092', '3099', '3101', '3103',
    #                    '3107', '3116', '3141', '3148', '3167', '3231', '3244', '3254', '3288', '3289', '3291', '3349',
    #                    '3360', '3382', '3391', '3401', '3402', '3405', '3407', '3436', '3543', '3549', '3563', '3626',
    #                    '3635', '3659', '3738', '3765', '3769', '3861', '3863', '3880', '3923', '3932', '3941', '4004',
    #                    '4005', '4021', '4042', '4043', '4061', '4063', '4088', '4091', '4151', '4182', '4183', '4188',
    #                    '4202', '4204', '4205', '4206', '4208', '4307', '4324', '4348', '4403', '4452', '4502', '4503',
    #                    '4506', '4507', '4516', '4519', '4521', '4523', '4527', '4528', '4536', '4543', '4552', '4553',
    #                    '4568', '4578', '4587', '4612', '4613', '4631', '4661', '4684', '4686', '4689', '4704', '4716',
    #                    '4732', '4739', '4751', '4755', '4768', '4812', '4816', '4819', '4848', '4849', '4887', '4901',
    #                    '4902', '4911', '4912', '4921', '4922', '4927', '4967', '5019', '5020', '5021', '5101', '5105',
    #                    '5108', '5110', '5201', '5202', '5214', '5232', '5233', '5301', '5332', '5333', '5334', '5393',
    #                    '5401', '5406', '5411', '5541', '5631', '5703', '5706', '5707', '5711', '5713', '5714', '5801',
    #                    '5802', '5803', '5857', '5929', '5947', '6005', '6028', '6035', '6055', '6098', '6103', '6113',
    #                    '6134', '6136', '6141', '6146', '6178', '6183', '6201', '6235', '6268', '6273', '6301', '6302',
    #                    '6305', '6326', '6361', '6367', '6383', '6432', '6448', '6465', '6471', '6472', '6473', '6479',
    #                    '6501', '6503', '6504', '6506', '6532', '6544', '6586', '6594', '6645', '6670', '6674', '6701',
    #                    '6702', '6703', '6723', '6724', '6727', '6728', '6750', '6752', '6753', '6754', '6758', '6762',
    #                    '6770', '6841', '6845', '6849', '6856', '6857', '6861', '6869', '6902', '6920', '6923', '6952',
    #                    '6954', '6965', '6971', '6976', '6981', '6988', '7003', '7004', '7011', '7012', '7013', '7148',
    #                    '7164', '7167', '7177', '7186', '7201', '7202', '7203', '7205', '7211', '7259', '7261', '7267',
    #                    '7269', '7270', '7272', '7276', '7282', '7309', '7313', '7419', '7453', '7459', '7516', '7532',
    #                    '7550', '7564', '7575', '7649', '7701', '7717', '7729', '7731', '7733', '7735', '7741', '7747',
    #                    '7751', '7752', '7762', '7832', '7846', '7911', '7912', '7947', '7951', '7956', '7974', '7988',
    #                    '8001', '8002', '8015', '8020', '8031', '8035', '8053', '8056', '8058', '8088', '8111', '8113',
    #                    '8194', '8233', '8252', '8253', '8267', '8273', '8279', '8282', '8283', '8303', '8304', '8306',
    #                    '8308', '8309', '8316', '8331', '8354', '8355', '8410', '8411', '8424', '8425', '8439', '8473',
    #                    '8570', '8572', '8585', '8591', '8593', '8595', '8601', '8604', '8628', '8630', '8697', '8725',
    #                    '8750', '8766', '8795', '8801', '8802', '8804', '8830', '8850', '8876', '8892', '8905', '8919',
    #                    '9001', '9005', '9007', '9008', '9009', '9020', '9021', '9022', '9042', '9062', '9064', '9065',
    #                    '9069', '9086', '9090', '9101', '9104', '9107', '9142', '9143', '9202', '9301', '9375', '9418',
    #                    '9432', '9433', '9434', '9435', '9501', '9502', '9503', '9504', '9506', '9508', '9509', '9513',
    #                    '9517', '9519', '9531', '9532', '9602', '9613', '9627', '9678', '9684', '9697', '9719', '9735',
    #                    '9744', '9766', '9787', '9810', '9843', '9962', '9983', '9984', '9989']
    js225_400_codes = [ '7752', '7762', '7832', '7846', '7911', '7912', '7947', '7951', '7956', '7974', '7988',
                       '8001', '8002', '8015', '8020', '8031', '8035', '8053', '8056', '8058', '8088', '8111', '8113',
                       '8194', '8233', '8252', '8253', '8267', '8273', '8279', '8282', '8283', '8303', '8304', '8306',
                       '8308', '8309', '8316', '8331', '8354', '8355', '8410', '8411', '8424', '8425', '8439', '8473',
                       '8570', '8572', '8585', '8591', '8593', '8595', '8601', '8604', '8628', '8630', '8697', '8725',
                       '8750', '8766', '8795', '8801', '8802', '8804', '8830', '8850', '8876', '8892', '8905', '8919',
                       '9001', '9005', '9007', '9008', '9009', '9020', '9021', '9022', '9042', '9062', '9064', '9065',
                       '9069', '9086', '9090', '9101', '9104', '9107', '9142', '9143', '9202', '9301', '9375', '9418',
                       '9432', '9433', '9434', '9435', '9501', '9502', '9503', '9504', '9506', '9508', '9509', '9513',
                       '9517', '9519', '9531', '9532', '9602', '9613', '9627', '9678', '9684', '9697', '9719', '9735',
                       '9744', '9766', '9787', '9810', '9843', '9962', '9983', '9984', '9989']


    for code in js225_400_codes:
        big_list = []
        try:

            big_list.append(code)

            url = "https://kabutan.jp/stock/finance?code={0}".format(code)
            jsp1 = JSPool_M1(url)  # 这里把请求和解析都进行了处理
            result1 = jsp1.page_parse_()

            url = "https://profile.yahoo.co.jp/fundamental/{0}".format(code)
            jsp2 = JSPool_M2(url)
            result2 = jsp2.page_parse_()
            f_list= big_list+list(result1)+list(result2)
            ff_l = []
            f_tup = tuple(f_list)
            ff_l.append((f_tup))
            print(big_list)
            print(ff_l)
            insertDB(ff_l)
            print(datetime.datetime.now())
        except IndexError:
            pass
    # big_list= []
    # excelFile = "JS225_400.xlsx"
    # full_items = read_xlrd(excelFile=excelFile)
    # for item in full_items:
    #     js225_400_codes.append(str(item[0])[0:4])
    #


# code,now_price,industry,bonus,name,manager,setuptime,listingtime,settleday,employee

#
# create table JS_manager(id int not null primary key auto_increment,
# code varchar(30),
# now_price varchar(30),
# industry varchar(30),
# bonus varchar(30),
# name varchar(30),
# manager varchar(30),
# setuptime varchar(30),
# listingtime varchar(30),
# settleday varchar(30),
# employee varchar(30),
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP ) engine=InnoDB  charset=utf8;



