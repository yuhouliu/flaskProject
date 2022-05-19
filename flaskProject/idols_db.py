# -*-coding: utf-8-*-
# 功能：创建数据库表
import sqlite3
import os
base_dir = os.path.dirname(__file__)

conn = sqlite3.connect('%s\idols.sqlite3' % base_dir)

cur = conn.cursor()

cur.execute('''
    create table idols(
         id integer primary key,
         name string(50),
         height string(50),
         age string(10),
         shows string(200))
 ''')

data = "1024, '张三', '178', '21', 'ewerrf'"
cur.execute('INSERT INTO idols VALUES (%s)' % data)
cur.fetchall()

cur.execute("select * from idols")
rows = cur.fetchall()
for row in rows:
    print(row)
    cur.execute("select name from sqlite_master where type='table' order by name")
    print(cur.fetchall())

    cur.execute("PRAGMA table_info(idols)")
    print(cur.fetchall())

    cur.close()
    conn.commit()
    conn.close()