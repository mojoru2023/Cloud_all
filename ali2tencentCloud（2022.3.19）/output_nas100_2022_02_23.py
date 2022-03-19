# !/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import datetime
import pymysql
import pandas as pd

from sqlalchemy import create_engine
import pymysql
import pandas as pd
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime

engine_Nas_Mons = create_engine('mysql+pymysql://root:123456@localhost:3306/NasMons')

output_code = 'AAPL,MSFT,AMZN,GOOG,GOOGL,FB,INTC,CMCSA,PEP,CSCO,ADBE,NVDA,NFLX,TSLA,COST,PYPL,AMGN,AVGO,TXN,CHTR,SBUX,QCOM,GILD,MDLZ,TMUS,FISV,BKNG,INTU,ADP,ISRG,VRTX,MU,CSX,BIIB,AMAT,AMD,ATVI,EXC,MAR,LRCX,WBA,ADI,ROST,ADSK,REGN,ILMN,CTSH,XEL,JD,MNST,MELI,NXPI,BIDU,KHC,SIRI,PAYX,EA,LULU,EBAY,CTAS,WDAY,ORLY,VRSK,WLTW,CSGP,PCAR,KLAC,SPLK,NTES,MCHP,VRSN,ANSS,IDXX,CERN,ALXN,ASML,SNPS,FAST,DLTR,CPRT,XLNX,CDNS,ALGN,SGEN,WDC,UAL,SWKS,CDW,CHKP,ULTA,INCY,TCOM,BMRN,EXPE,MXIM,CTXS,TTWO,FOXA,AAL,NTAP,FOX,LBTYK,LBTYA,IXIC,LastTime'

sql_Nas_Mons = 'select * from nas100_2022_02_23  ; '

ln = os.getcwd()


def savedt():

    df_js225 = pd.read_sql_query(sql_Nas_Mons, engine_Nas_Mons)
    excelFile3 = '{0}/{1}.xlsx'.format(ln, "nas100_2022_02_23")  # 处理了文件属于当前目录下！
    df_js225.to_excel(excelFile3)





if __name__ == '__main__':
    savedt()

# 0 19 1,15 * *  /usr/local/bin/python3.6 /root/cron_Nas_Mons.py
# 每个月的1号的19点钟运行xxx.sh
# 分钟、小时、日子可以更改，后两项为*就是monthly。
