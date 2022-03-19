

# !/usr/bin/python
# -*- coding: UTF-8 -*-


from sqlalchemy import create_engine

import pandas as pd

from l_p_config import *

def savedt():
    for one_month in month_dbname:
        engine_jsMons = create_engine('mysql+pymysql://root:123456@localhost:3306/JS')
        sql_sp_LJ = 'select id from {0}  ; '.format(one_month)

        df_js = pd.read_sql_query(sql_sp_LJ.format(one_month), engine_jsMons)
        df_list = df_js.values.tolist()
        max_id = max([x[0] for x in df_list])
        selec_contions =all_code +["LastTime"]
        sql_sp_f = 'select {2} from {0}  where id ={1} ; '
        df_js_f = pd.read_sql_query(sql_sp_f.format(one_month,max_id,",".join(selec_contions)), engine_jsMons)
        df_js_f.to_excel("{0}.xlsx".format(one_month))



if __name__ == '__main__':
    savedt()



