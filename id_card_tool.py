# !/usr/bin/python3
# -*- coding: utf-8 -*-


import urllib.request
import json

while True:
    car_no = input("请输入身份证号：")
    url = "http://api.itmojun.com/idcard?cardno=%s"% car_no
    rsq = urllib.request.urlopen(url).read().decode()
    id_card_info = json.loads(rsq)

    if id_card_info["err"]:
        print("身份证格式错误!")
    else:
        print("地区：{}\n生日: {}\n性别：{}" .format(id_card_info["area"],id_card_info["birthday"],id_card_info["sex"]))








