"""
    tornado web app对于网页模板的处理和静态文件的操作
    网页模板：html页面
    处理：定义html页面、渲染html页面，响应html页面[浏览器]
    静态资源：图片/js/css/字体...
    操作：配置静态资源、查询静态资源[html]、响应数据
"""

# 引入需要的模块
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from tornado.options import define, options, parse_command_line
from tornado.httpserver import HTTPServer
import os.path
import json
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 显示中文
# 定义变量
define("port", default=8009, help="默认端口8000")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost/JS_Mons'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

Base = declarative_base()

# sqlalchemy 对已有表做操作需要先做一个映射类

class FJSs(Base):
    __tablename__ = 'FJSs'
    id = Column(Integer,primary_key=True,nullable=False, autoincrement=True)
    js_225_4000 = Column(String(12),nullable=True)  # String在数据库中常见为varchar类型



    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict


# 创建视图类
class IndexHandler(RequestHandler):
    def get(self):
        big_list = []
        pls = db.session.query(FJSs.js_225_4000).all()  # [[0.19],[0.19]] 需要两层遍历来做一个大列表
        for item in pls:
            for i in item:
                num_int = float(i)
                big_list.append(num_int)  # 需要把字符串类型转换为浮点型,而不是整型
        # 有时候需要用int()函数转换字符串为整型，但是切记int()只能转化由纯数字组成的字符串，如下例：a
        t = {}
        t['data'] = big_list
        f_json = json.dumps(t)
        self.write(f_json)



class Image(RequestHandler):
    def get(self):
        self.render("fjss_api.html")





# 程序入口
if __name__ == '__main__':
    # 开始监听
    parse_command_line()
    app = Application(
        [
            (r"/data", IndexHandler),
            (r"/fjss", Image),
        ],

        # 项目配置信息
        # 网页模板
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        # 静态文件
        static_path=os.path.join(os.path.dirname(__file__), "static"),

        debug=True
    )

    # 部署
    server = HTTPServer(app)
    server.listen(options.port)

    # 轮询监听
    IOLoop.current().start()