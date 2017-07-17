#!/usr/bin/env python
#coding=utf-8

from pyecharts import Polar

def test_polar():

    # polar_0
    import random
    data = [(i, random.randint(1, 100)) for i in range(101)]
    polar = Polar("极坐标系-散点图示例")
    polar.add("", data, boundary_gap=False, type='scatter', is_splitline_show=False, is_axisline_show=True)
    polar.show_config()
    polar.render()

    # polar_1
    data_1 = [(10, random.randint(1, 100)) for i in range(300)]
    data_2 = [(11, random.randint(1, 100)) for i in range(300)]
    polar = Polar("极坐标系-散点图示例", width=1200, height=600)
    polar.add("", data_1, type='scatter')
    polar.add("", data_2, type='scatter')
    polar.show_config()
    polar.render()

    # porlar_2
    data = [(i, random.randint(1, 100)) for i in range(10)]
    polar = Polar("极坐标系-动态散点图示例", width=1200, height=600)
    polar.add("", data, type='effectScatter', effect_scale=10, effect_period=5)
    polar.show_config()
    polar.render()

    # polar_3
    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
    polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
    polar.show_config()
    polar.render()

    # polar_4
    radius = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    polar = Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
    polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
    polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
    polar.show_config()
    polar.render()

    # polar_5
    import math
    data = []
    for i in range(101):
        theta = i / 100 * 360
        r = 5 * (1 + math.sin(theta / 180 * math.pi))
        data.append([r, theta])
    hour = [i for i in range(1, 25)]
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Love", data, angle_data=hour, boundary_gap=False, start_angle=0)
    polar.show_config()
    polar.render()

    # polar_6
    data = []
    for i in range(361):
        t = i / 180 * math.pi
        r = math.sin(2 * t) * math.cos(2 * t)
        data.append([r, i])
    polar = Polar("极坐标系示例", width=1200, height=600)
    polar.add("Flower", data, start_angle=0, symbol=None, axis_range=[0, None])
    polar.show_config()
    polar.render()