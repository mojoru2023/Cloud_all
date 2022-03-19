import pymysql
import pandas as pd
from plotnine import *
import pandas as pd
from sqlalchemy import create_engine


def get_local_data():
    # 初始化数据库连接，使用pymysql模块
    # MySQL的用户：root, 密码:147369, 端口：3306,数据库：test
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/JS_Mons')
    # 查询语句，选出employee表中的所有数据

    sql_table_count = "SELECT js_225_4000  FROM FJSs  "
    sql_table_long = pd.read_sql_query(sql_table_count, engine)

    where_conditons = [i for i in  range(1,sql_table_long.iloc[:, 0].size,20)]
    sql_cmd = "SELECT *  FROM FJSs  where id in {0}".format(tuple(where_conditons))
    # read_sql_query的两个参数: sql语句， 数据库连接
    sql_pandas = pd.read_sql_query(sql_cmd, engine)
    print(sql_pandas)

    pg =ggplot(aes(x='id', y='js_225_4000'), data=sql_pandas) + \
    geom_line() + \
    stat_smooth(color='blue', span=0.2, method='loess')
    ggsave(pg, "js255_400.svg")









get_local_data()













