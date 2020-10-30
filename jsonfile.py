
# -*- coding=utf-8 -*-
__author__ = '-ling'


import os
import sys
import time
import json
import shutil
import configparser


class Json_File_Man(Gen_File_handle):
    """
        Json 文件 增删改查
        继承 Man_File_handle
    """

    def __init__(self, file_path):
        # 先继承，再构造
        # 继承父类的构造方法
        Gen_File_handle.__init__(self, file_path)

    def class_name(self):
        print("Json_File_Man --> Man_File_handle.")

    # 增
    def add_json_data(self, datas):
        if self.examine_file() == True:
            with open(self.file_path, 'a+', encoding='utf-8') as file:
                input_data = str(datas)
                # 过滤处理  处理 '\n'
                input_data = input_data.replace("\n", "")
                # 如果是第一个字符没有 { 最后一个字符没有 } 则加上
                if input_data[0] != '{':
                    input_data = '{' + input_data
                if input_data[-1] != '}':
                    input_data = input_data + '}'
                # 有与 json 字符串不支持 ' 则改为 "
                input_data = input_data.replace("\'", "\"")
                # print(type(input_data))
                file.write(input_data + "\n")

    # 删
    def del_json_data(self, datas):
        print('del_json_data')
        if self.examine_file() == True:
            pass

    # 改
    def update_json_data(self, datas):
        print('update_json_data')
        if self.examine_file() == True:
            pass

    # 查
    def select_json_data(self, datas):
        print('select_json_data')
        if self.examine_file() == True:
            pass

