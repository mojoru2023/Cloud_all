#! -*- coding:utf-8 -*-


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






def insertDB(content):
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='NasMons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)

    cursor = connection.cursor()
    try:

        f_104 = "%s," *104
        cursor.executemany('insert into nas100_2022_02_23 ({0}) values ({1})'.format(nasdap100,f_104[:-1]), content)
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

        url = "http://gu.qq.com/us{0}.OQ/gg".format(code)
        html = call_page(url)
        parse_html(html)
        print(big_list)
        print(url)
    ff_l = []
    f_tup = tuple(big_list)
    ff_l.append((f_tup))
    insertDB(ff_l)






 #create table nas100_2022_02_23(id int not null primary key auto_increment,AAPL  float,MSFT  float,AMZN  float,GOOG  float,GOOGL  float,FB  float,INTC  float,CMCSA  float,PEP  float,CSCO  float,ADBE  float,NVDA  float,NFLX  float,TSLA  float,COST  float,PYPL  float,AMGN  float,AVGO  float,TXN  float,CHTR  float,SBUX  float,QCOM  float,GILD  float,MDLZ  float,TMUS  float,FISV  float,BKNG  float,INTU  float,ADP  float,ISRG  float,VRTX  float,MU  float,CSX  float,BIIB  float,AMAT  float,AMD  float,ATVI  float,EXC  float,MAR  float,LRCX  float,WBA  float,ADI  float,ROST  float,ADSK  float,REGN  float,ILMN  float,CTSH  float,XEL  float,JD  float,MNST  float,MELI  float,NXPI  float,BIDU  float,KHC  float,SIRI  float,PAYX  float,EA  float,LULU  float,EBAY  float,CTAS  float,WDAY  float,ORLY  float,VRSK  float,WLTW  float,CSGP  float,PCAR  float,KLAC  float,SPLK  float,NTES  float,MCHP  float,VRSN  float,ANSS  float,IDXX  float,CERN  float,ALXN  float,ASML  float,SNPS  float,FAST  float,DLTR  float,CPRT  float,XLNX  float,CDNS  float,ALGN  float,SGEN  float,WDC  float,UAL  float,SWKS  float,CDW  float,CHKP  float,ULTA  float,INCY  float,TCOM  float,BMRN  float,EXPE  float,MXIM  float,CTXS  float,TTWO  float,FOXA  float,AAL  float,NTAP  float,FOX  float,LBTYK  float,LBTYA  float ,IXIC float, LastTime timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP) engine=InnoDB  charset=utf8;


# drop table nasdap100_s;


# mei
#*/3 * * * * /home/w/pyenv/bin/python /home/w/SP500_Nasdap100/SP500.py
