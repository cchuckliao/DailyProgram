import redis
from A0001 import generate_coupon


def add_to_redis(lst):
    pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
    r = redis.StrictRedis(connection_pool=pool)  # 连接池
    print(r.llen('coupons_2'))
    r.ltrim('coupons_2', 1, 0)  # 删除索引之外的值。索引起始值比索引结束值大的时候则清空列表
    r.rpush('coupons_2', *lst)  # 将列表转化为多个值，插入到coupons_2这个列表中
    print(r.lrange('coupons_2', 0, -1))
    print(r.llen('coupons_2'))


if __name__ == '__main__':
    coupons = generate_coupon(10, 200)
    add_to_redis(coupons)
