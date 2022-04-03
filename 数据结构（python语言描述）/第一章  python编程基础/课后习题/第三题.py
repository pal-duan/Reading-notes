def get_bounce_distance(init_height, count):
    """
    输入球的初始高度以及允许球持续弹跳的次数，输出球所运动的总距离
    :param init_height:
    :param count:
    :return:
    """
    res = 0
    while count:
        res += init_height + init_height * 0.6
        init_height *= 0.6
        count -= 1
    return res + init_height


print(get_bounce_distance(10, 2))