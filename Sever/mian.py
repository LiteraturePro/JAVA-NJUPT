# -*- coding: utf8 -*-
import os
import requests
import pymysql
import time
import datetime
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler
from multiprocessing import Process


## 初始化调度器
scheduler = BlockingScheduler()



# 防止敏感信息泄漏，在云函数端采用环境变量的方式接收相应的参数值，在相应的云函数环境配置环境变量

user_name = os.environ.get('user_name')
password = os.environ.get('password')
address = os.environ.get('address')
port = os.environ.get('port')
database_name = os.environ.get('database_name')
table_name = os.environ.get('table_name')
sckey = os.environ.get('sckey')        #方糖推送
spkey = os.environ.get('spkey')       #CoolPush酷推




def Read_database (user_name,password,address,port,database_name,table_name):
    """读取数据库中表'tasks'中的所有数据.
    完成数据库消息数据的读取，返回数据列表，方便后续任务调度器的使用.
    
    Args:
        user_name: 数据库用户名.
        password: 数据库密码.
        address: 数据库地址.
        port: 数据库端口.
        database_name: 数据库名.
        table_name: 数据库中数据表名.
    Returns:
        返回数据库中‘did’字段为‘0’的所有数据. 
        For example:
        {                                 ID  year  month  day  hour  minute       text    did
         0  f83973ecf99a11ea928300163e2c040a  2020      9   20    17      30  提醒我吃饭     0  }
    Raises:
        IOError: None.
    """
    # sql = '''SELECT * from '''+table_name+''';'''       # 读取所有数据
    
    # 读取字段did为0的所有数据
    sql = '''SELECT * from '''+table_name+''' where did = 0;'''       
    conn = pymysql.connect(host = address,user = user_name,passwd = password,\
                           db = database_name , port = int(port) ,charset = "utf8mb4")
    try:
        df = pd.read_sql (sql,con = conn)
    except:
        print ('\n Reading Error  \n')    
    finally:
        # 关闭连接
        conn.close()
    print ('\n Completion of data reading \n')    
    return (df) 


def Update_database(user_name,password,address,port,database_name,table_name,ID):
    """更新数据库中表中的所有已经执行过数据.
    完成数据库消息数据的更新.

    Args:
        user_name: 数据库用户名.
        password: 数据库密码.
        address: 数据库地址.
        port: 数据库端口.
        database_name: 数据库名.
        table_name: 数据库中数据表名.
        ID: 一条数据信息的UUID.
    Returns:
        None.
    Raises:
        IOError: None.
    """
    conn = pymysql.connect(host = address,user = user_name,passwd = password,\
                           db = database_name , port = int(port) ,charset = "utf8mb4")
    # 使用cursor()方法获取操作游标 
    cursor = conn.cursor()
    # SQL 更新语句
    sql = "UPDATE tasks SET did = 1 WHERE ID = '%s'" % (ID)
    
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        conn.commit()     
    except:
        # 发生错误时回滚
        conn.rollback()
        print ('\n Updating Error  \n')    
    finally:
        # 关闭连接
        conn.close()
    print ('\n Completion of data updating \n')    


def task_dispatch(data):
    """并行任务调度器.
    完成并发任务的调度.

    Args:
        data: 任务列表.
    Returns:
        None.
    Raises:
        IOError: None.
    """
    
    # 定义调度参数
    text = data[6]
    time_data = data[1]+"-"+data[2]+"-"+data[3]+" "+data[4]+":"+data[5]+":00"
    
    # 调度方式示例
    #scheduler.add_job(func=aps_test, args=('定时任务',), trigger='cron', second='*/5')
    #scheduler.add_job(func=aps_test, args=('一次性任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
    #scheduler.add_job(func=aps_test, args=(text,), trigger='date', run_date=time_data)
    #scheduler.add_job(func=aps_test, args=('循环任务',), trigger='interval', seconds=3)
    #scheduler.add_job(func=aps_pause, args=('一次性任务,停止循环任务',), next_run_time=datetime.datetime.now() + datetime.timedelta(seconds=12))
    
    # 将调度任务写入内存，用于后台执行
    scheduler.add_job(func=text_push, args=(data,), trigger='date', run_date=time_data)
    try:
        print(scheduler.get_jobs())
        # 调度开始
        scheduler.start()
    except SystemExit:
        scheduler.shutdown()
        print("调度出错")



def Data_dispose(datalist):

    # 处理Severless中系统时间比实际时间少8个小时
    if time.localtime().tm_hour <= 16:
        print(time.localtime().tm_hour)
        time_hour = time.localtime().tm_hour+8
    elif time.localtime().tm_hour == 17:
        print(time.localtime().tm_hour)
        time_hour = 1
    elif time.localtime().tm_hour == 18:
        print(time.localtime().tm_hour)
        time_hour = 2
    elif time.localtime().tm_hour == 19:
        print(time.localtime().tm_hour)
        time_hour = 3
    elif time.localtime().tm_hour == 20:
        print(time.localtime().tm_hour)
        time_hour = 4
    elif time.localtime().tm_hour == 21:
        print(time.localtime().tm_hour)
        time_hour = 5
    elif time.localtime().tm_hour == 22:
        print(time.localtime().tm_hour)
        time_hour = 6
    elif time.localtime().tm_hour == 23:
        print(time.localtime().tm_hour)
        time_hour = 7
    elif time.localtime().tm_hour == 24:
        print(time.localtime().tm_hour)
        time_hour = 8
    else :
        print("假的吧，还有这事?")


    # 格式化时间戳为本地的时间
    time_year = time.localtime().tm_year
    time_month = time.localtime().tm_mon
    time_day = time.localtime().tm_mday
    time_min = time.localtime().tm_min
    print(time_year,time_month,time_day,time_hour,time_min)
    
    final_list = []

    for data in datalist:
        # 计算任务时间差
        time_diff = int(data[5])-time_min

        if int(data[1]) == time_year and int(data[2]) == time_month and int(data[3]) == time_day and int(data[4]) == time_hour and (time_diff > 0) and (time_diff <= 1):
            
            # 将要完成的任务装载一个列表
            final_list.append(data)
            
            # 将完成的任务写回数据库并标记为已执行
            Update_database(user_name,password,address,port,database_name,table_name,data[0])
        else:
            print("时间没到")
            #final_list.append(data)
            
    return final_list



def text_push(data):
    """消息推送.
    完成消息队列中定时任务的消息推送.
    
    Args:
        text: 需要推送的消息.
    Returns:
        None.
    Raises:
        IOError: None.
    """ 
    text = data[6]
    time_year = time.localtime().tm_year
    time_month = data[2]
    time_day = data[3]
    time_hour = data[4]
    time_min = data[5]
    
    # 构造消息格式
    qq_text="     【今日提醒任务】     \n"+"🕙:    "+str(time_year)+"-"+str(time_month)+"-"+str(time_day)+" "+str(time_hour)+":"+str(time_min)+":00"+"\n"+"🍄:    "+text+"\n"
    wechat_text="     【🕙:    "+str(time_year)+"-"+str(time_month)+"-"+str(time_day)+" "+str(time_hour)+":"+str(time_min)+":00】"+"\n\n"+"     【🍄:    "+text+"】     \n"
    
    """微信公众号消息推送"""
    title = "【今日任务提醒】"
    requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+title+'&desp=' + wechat_text)
    
    """QQ号消息推送""" 
    cpurl = 'https://push.xuthus.cc/send/'+spkey    #发送方式，我用的send
    requests.post(cpurl,qq_text.encode('utf-8'))         #把天气数据转换成UTF-8格式，不然要报错。
    
    # 关闭调度器
    scheduler.shutdown(wait=False)
    
    
    
def main():
    # 从数据库获得数据
    df = Read_database (user_name,password,address,port,database_name,table_name)
    
    datalist=df.values
    print(datalist)
    # 将倒计时还剩一分钟的数据提取
    do_list = Data_dispose(datalist)
    print(do_list)
    # 开启多进程完成并发隔离任务
    for i in do_list:
        print(i)
        # 线程装载
        p=Process(target=task_dispatch,args=(i,))
        # 启动进程，完成并发调度
        p.start()
        

# 云函数入口
def main_handler(event, context):
    main()
