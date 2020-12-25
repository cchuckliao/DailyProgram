from A0001 import generate_coupon
import pymysql
from pymysql.cursors import DictCursor

coupons = generate_coupon(10, 200)

connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='qingdidala', db='db1', charset='utf8')
cursor = connection.cursor()
sql = "INSERT INTO t2(coupon) VALUES(%s)"

try:
    cursor.executemany(sql, coupons)
    cursor.connection.commit()
except Exception as e:
    print(e)

cursor.close()
connection.close()