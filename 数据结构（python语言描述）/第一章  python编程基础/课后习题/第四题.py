def get_pi(count):
    res = 0
    s = 1
    flag = 1
    while count:
        res += flag * (1 / s)
        s += 2
        flag *= -1
        count -= 1
    return res * 4


print(get_pi(1000000))