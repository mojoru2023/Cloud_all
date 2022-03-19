#! -*- coding:utf-8 -*-


import datetime
import re
import time

import pymysql
import requests
from lxml import etree
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
from selenium import webdriver


def use_selenium_headless(url):
    ch_options = webdriver.ChromeOptions()
    # 为Chrome配置无头模式
    ch_options.add_argument("--headless")
    ch_options.add_argument('--no-sandbox')
    ch_options.add_argument('--disable-gpu')
    ch_options.add_argument('--disable-dev-shm-usage')
    # 在启动浏览器时加入配置
    dr = webdriver.Chrome(options=ch_options)
    dr.get(url)
    return dr.page_source




def use_requests(url):

    response = requests.get(url)
    return response.text

def getinfos_fromGoogleFinance(code):
    url = "https://www.google.com/finance/quote/{0}:NASDAQ?hl=zh-CN".format(code)
    html = use_requests(url)
    selector = etree.HTML(html)
    title_zh_cn = selector.xpath('//*[@id="yDmH0d"]/c-wiz/div/div[4]/div/div/main/div[1]/div[2]/text()')
    pattern = re.compile('<div class="bLLb2d">(.*?)<a target="_blank" rel=".*?" href=".*?" class=".*?">Wikipedia</a>',re.S)
    infos_zh_cn = re.findall(pattern,html)
    time.sleep(0.1)
    return title_zh_cn,infos_zh_cn







def getinfos_fromYhaooFinance(code):
    url = "https://finance.yahoo.com/quote/{0}/profile?p={0}".format(code)
    html = use_selenium_headless(url)
    selector = etree.HTML(html)
    industry_infos = selector.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[4]/text()')
    sector_infos = selector.xpath('//*[@id="Col1-0-Profile-Proxy"]/section/div[1]/div/div/p[2]/span[2]/text()')
    return industry_infos,sector_infos








def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='Nas100_infos',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:
        cursor.executemany('insert into nas100_industry_infos (code,title_zh_cn,industry_infos,sector_infos,infos_zh_cn) values (%s,%s,%s,%s,%s)', content)
        connection.commit()
        connection.commit()
        connection.close()
        print('向MySQL中添加数据成功！')
    except TypeError :
        pass



if __name__ == '__main__':
    big_list = []
    nasdap100 = 'AAPL,MSFT,AMZN,GOOG,GOOGL,FB,INTC,CMCSA,PEP,CSCO,ADBE,NVDA,NFLX,TSLA,COST,PYPL,AMGN,AVGO,TXN,CHTR,SBUX,QCOM,GILD,MDLZ,TMUS,FISV,BKNG,INTU,ADP,ISRG,VRTX,MU,CSX,BIIB,AMAT,AMD,ATVI,EXC,MAR,LRCX,WBA,ADI,ROST,ADSK,REGN,ILMN,CTSH,XEL,JD,MNST,MELI,NXPI,BIDU,KHC,SIRI,PAYX,EA,LULU,EBAY,CTAS,WDAY,ORLY,VRSK,WLTW,CSGP,PCAR,KLAC,SPLK,NTES,MCHP,VRSN,ANSS,IDXX,CERN,ALXN,ASML,SNPS,FAST,DLTR,CPRT,XLNX,CDNS,ALGN,SGEN,WDC,UAL,SWKS,CDW,CHKP,ULTA,INCY,TCOM,BMRN,EXPE,MXIM,CTXS,TTWO,FOXA,AAL,NTAP,FOX,LBTYK,LBTYA,IXIC'
    f_nas100 =nasdap100.split(",")
    for code in f_nas100:
        title_zh_cn,infos_zh_cn = getinfos_fromGoogleFinance(code)
        industry_infos,sector_infos = getinfos_fromYhaooFinance(code)
        s_item = [code] + title_zh_cn+ industry_infos+ sector_infos+infos_zh_cn
        print(code,title_zh_cn,industry_infos,sector_infos,infos_zh_cn)
        f_tuple = tuple(s_item)
        finanl_content = [f_tuple]
        insertDB(finanl_content)








#  create table nas100_industry_infos
# (id int not null primary key auto_increment,
# code  text,
# title_zh_cn text,
# industry_infos text,
# sector_infos text,
# infos_zh_cn  text,
# LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table nas100_industry_infos;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py
