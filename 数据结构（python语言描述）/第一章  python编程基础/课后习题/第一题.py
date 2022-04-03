from math import pi
import trafaret as tft
"""
输入球体半径，输出球体的直径、圆周长、表面积、体积
"""


radius = input("请输入球体半径：")
radius = tft.ToFloat().check(radius)


def get_diameter(radius):
    """
    球体的直径
    :param radius:
    :return:
    """
    return radius * 2


def get_circumference(radius):
    """
    球体的圆周长
    :param radius:
    :return:
    """
    return 2 * pi * radius


def get_surface_area(radius):
    """
    球体的表面积
    :param radius:
    :return:
    """
    return 4 * pi * radius ** 2


def get_volume(radius):
    """
    球体的体积
    :param radius:
    :return:
    """
    return 4 / 3 * pi * radius ** 3


print(f"球体的直径为：{get_diameter(radius)}")
print(f"球体的圆周长为：{get_circumference(radius)}")
print(f"球体的表面积为：{get_surface_area(radius)}")
print(f"球体的体积为：{get_volume(radius)}")
