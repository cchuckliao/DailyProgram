import random


def generate_coupon(length, amount):
    letters = [str(i) for i in range(0, 10)]
    for i in (list(range(65, 91)) + list(range(97, 123))):
        letters.append(chr(i))
    coupons = []
    for i in range(amount):
        coupon = []
        for j in range(length):
            coupon.append(random.choice(letters))
        coupons.append(''.join(coupon))
    return coupons


if __name__ == '__main__':
    print(generate_coupon(20, 10))
