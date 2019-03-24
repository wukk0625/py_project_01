# -*- coding : utf-8 -*-
import pymysql

# 打开数据库连接
db = pymysql.connect(host="localhost", user="root",
                     password="111111", db="demo", port=3306)
print(db)
# 使用cursor()方法获取操作游标
cur = db.cursor()

# 1.查询操作
# 编写sql 查询语句  user 对应我的表名
sql = "select * from user"
try:
    cur.execute(sql)  # 执行sql语句

    results = cur.fetchall()  # 获取查询的所有记录
    print("id", "name", "password")
    # 遍历结果
    for row in results:
        id = row[0]
        name = row[1]
        password = row[2]
        print(id, name, password)
except Exception as e:
    raise e
finally:
    db.close()  # 关闭连接
