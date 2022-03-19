


# https://www.mql5.com/zh/docs/integration/python_metatrader5

# 1. 取mt5数据 m15
# 2. 每10秒测试一次，close-open 大于80 ，就发送信号
# 3. 云服务器向手机微信发送通知
# Greenbirch2007
# NDUEg49y


from datetime import datetime
import MetaTrader5 as mt5

# 显示有关MetaTrader 5程序包的数据
print("MetaTrader5 package author: ", mt5.__author__)
print("MetaTrader5 package version: ", mt5.__version__)

# 导入'pandas'模块，用于以表格形式显示获得的数据
import pandas as pd

pd.set_option('display.max_columns', 500)  # number of columns to be displayed
pd.set_option('display.width', 1500)  # max table width to display
# 导入用于处理时区的pytz模块
import pytz


def minum_15m(string_datetime):
    import datetime
    string_datetime = datetime.datetime.strptime(string_datetime, "%Y-%m-%d %H:%M")  # 把strTime转化为时间格式,后面的秒位自动补位的
    startTime2 = (string_datetime + datetime.timedelta(minutes=-15)).strftime("%Y-%m-%d %H:%M")
    return startTime2
# 建立与MetaTrader 5程序端的连接
if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

# set time zone to UTC
timezone = pytz.timezone("Etc/UTC")
# create 'datetime' object in UTC time zone to avoid the implementation of a local time zone offset
utc_from = datetime(2022,3,8, tzinfo=timezone)
# request 100 000 EURUSD ticks starting from 10.01.2019 in UTC time zone
ticks = mt5.copy_ticks_from("NI225", utc_from, 10000, mt5.COPY_TICKS_ALL)
print("Ticks received:", len(ticks))

# shut down connection to the MetaTrader 5 terminal
mt5.shutdown()

# display data on each tick on a new line
# print("Display obtained ticks 'as is'")
# count = 0
# for tick in ticks:
#     count += 1
#     print(tick)
#     if count >= 10:
#         break

# create DataFrame out of the obtained data
ticks_frame = pd.DataFrame(ticks)
# 将时间（以秒为单位）转换为日期时间格式
ticks_frame['time'] = pd.to_datetime(ticks_frame['time'], unit='s')

# 整体处理 #直接 1000就好
# 求一个平均差即可！如果！
the_last_dt_3000 = ticks_frame.tail(3000)
the_last_row = the_last_dt_3000.tail(1)
last_time = str(list(the_last_row["time"])[0])
print(last_time)
def minum_15m(string_datetime):
    import datetime
    string_datetime = datetime.datetime.strptime(string_datetime, "%Y-%m-%d %H:%M:%S")  # 把strTime转化为时间格式,后面的秒位自动补位的
    startTime2 = (string_datetime + datetime.timedelta(minutes=-15)).strftime("%Y-%m-%d %H:%M:%S")
    return startTime2
_15_time = minum_15m(last_time)
the_first_row = the_last_dt_3000.loc[the_last_dt_3000['time']=="{0}".format(_15_time)]

print(the_first_row)
print(the_last_row)




# # str---->datetime -15------> str
# last_time_str_datetime = datetime.strptime(last_time,"%Y-%m-%d %H:%M:%S")
#
# print(last_time_str_datetime)
# print(_15_time)




#                      time      bid      ask  last  volume       time_msc  flags  volume_real
# 46508 2022-03-08 11:50:31  24822.0  24830.0   0.0       0  1646740231602      6          0.0
#                      time      bid      ask  last  volume       time_msc  flags  volume_real
# 47507 2022-03-08 12:09:09  24780.0  24787.0   0.0       0  1646741349254      6          0.0




