# encoding: utf-8

"""
date: 2021/01/23/00/48

"""

import pymysql

def get_conn():
    return  pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root759967211',
        database='python_mysql',
        charset='utf8'
    )

def query_data(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(sql)
        return cursor.fetchall()
    finally:
        conn.close()

def inser_or_update(sql):
    conn = get_conn()
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
    finally:
        conn.close()

if __name__ == '__main__':
    sql = "insert into user (name, sex, age, email) values ('xiaobai','woman',18,'xiaobai@qq.com');"
    inser_or_update(sql)
    sql = "select * from user"
    data = query_data(sql=sql)
    import pprint
    pprint.pprint(data)


