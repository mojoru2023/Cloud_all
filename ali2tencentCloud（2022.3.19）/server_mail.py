


# coding:utf-8
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import pymysql
import pandas as pd
from plotnine import *
import pandas as pd
from sqlalchemy import create_engine
import os


from email.mime.base import MIMEBase
from email.header import Header
import smtplib
from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText
import email.encoders as Encoders
import os
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import datetime
import smtplib


ln = os.getcwd()

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文

def get_local_data():
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/JS_Mons')
    # 查询语句，选出employee表中的所有数据

    sql_table_count = "SELECT js_225_4000  FROM FJSs  "
    sql_table_long = pd.read_sql_query(sql_table_count, engine)
    # 
    where_conditons = [i for i in  range(1,sql_table_long.iloc[:, 0].size,1)]
    sql_cmd = "SELECT *  FROM FJSs  where id in {0}".format(tuple(where_conditons))
    # read_sql_query的两个参数: sql语句， 数据库连接
    sql_pandas = pd.read_sql_query(sql_cmd, engine)
    print(sql_pandas)

    pg =ggplot(aes(x='id', y='js_225_4000'), data=sql_pandas) + \
    geom_line() + \
    stat_smooth(color='blue', span=0.2, method='loess')
    ggsave(pg, "js255_400.svg")








def sendto_wechat():


    gmail_user = "min2020fr@gmail.com"
    gmail_pwd = "dwodwugqviervgjo"

    to = "min2020fr@gmail.com"
    subject = "Report"
    text = "Picture report"
    attach = 'js255_400.svg'

    msg = MIMEMultipart()

    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    Encoders.encode_base64(part)
    part.add_header('Content-Disposition',
                    'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, to, msg.as_string())
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()



if __name__ =="__main__":
    get_local_data()
    sendto_wechat()

