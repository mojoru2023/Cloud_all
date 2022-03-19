import pymysql
import csv
import os

# 数据处理好，看如何塞入execl中


def csv_dict_write(path, head, data):
    with open(path, 'w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, head)
        writer.writeheader()
        writer.writerows(data)
        return True


if __name__ == '__main__':
    l_path = os.getcwd()
    connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='JS_Mons',
                                 charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cur = connection.cursor()

    count_sql = "select count(*) from JS_manager; "
    cur.execute(count_sql)
    long_count = cur.fetchone()['count(*)']
    # sql 语句
    big_list = []
    for num in range(1, long_count):
        sql = 'select code,now_price,industry,bonus,name,manager,setuptime,listingtime,settleday,employee  from JS_manager where id = %s ' % num
        # #执行sql语句
        cur.execute(sql)
        # #获取所有记录列表
        data = cur.fetchone()
        big_list.append(data)

    # #执行sql语句
# salary,type,link,job_name
    head = ["code","now_price","industry","bonus","name","manager","setuptime","listingtime","settleday","employee"]
    csv_dict_write('{0}/JS_manager.csv'.format(l_path), head, big_list)
    print("数据导出完成～")
