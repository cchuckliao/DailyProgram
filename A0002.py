from A0001 import generate_coupon
import pymysql
from pymysql.cursors import DictCursor

coupons = generate_coupon(10, 200)

connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='qingdidala', db='db1', charset='utf8')
cursor = connection.cursor()
sql = "INSERT INTO t3(no, coupon) VALUES(%s,%s)"
to_add = []
for i in range(len(coupons)):
    to_add.append((str(i+1), coupons[i])) #为了不报错，把数字改为字符，数据库对应列的类型也改为字符。

print(to_add)
try:
    cursor.executemany(sql, to_add)
    cursor.connection.commit()
except Exception as e:
    print(e)

cursor.close()
connection.close()
