
# -*- coding=utf-8 -*-
__author__ = '-ling'


import os
import sys
import time
import json
import shutil
import configparser


class Ini_File_Man(Gen_File_handle):
    """
        ini 文件 增删改查
        继承 Man_File_handle
    """

    def __init__(self, file_path, cfg_debug=False):
        Gen_File_handle.__init__(self, file_path)
        # super(Man_File_handle, self).__init__()
        # self.file_path = file_path
        self.config = configparser.ConfigParser()
        # 开启 debug模式
        self.cfg_debug = cfg_debug

    # __read_ini_file #__init__()  无法返回值，能不规避报错，所有写成方法 __read_ini_file()

    # 读取 ini 文件
    def __read_ini_file(self):
        if self.examine_file() == True:
            try:
                self.config.read(self.file_path)
            except Exception as e:
                if self.cfg_debug == True:
                    print(e)
                else:
                    pass

    # input ini 文件 提交操作
    def __submit_operation(self):
        self.config.write(open(self.file_path, "w"))

    def class_name(self):
        print("Ini_File_Man --> Man_File_handle.")

    # 获取所有的 sections
    def get_all_sections(self):
        self.__read_ini_file()
        lists_header = self.config.sections()
        return lists_header

    # 获取默认值 的所有信息
    def get_default_data(self):
        self.__read_ini_file()
        return self.config.defaults()

    # 获取 指定 section item 的值
    def get_section_item_value(self, section, item):
        self.__read_ini_file()
        try:
            value = self.config.get(section, item)
            return value
        except Exception as e:
            print("repetition data")

    # 获取 指定 section 所有 item
    # 返回列表
    def get_section_item(self, section):
        self.__read_ini_file()
        item_list = []
        for item in self.config[section]:
            # print(item)
            item_list.append(item)
        return item_list

    # 获取节section点下所有option的key，包括默认option
    def get_section_option(self, section):
        self.__read_ini_file()
        return self.config.options(section)

    # 获取取节section点下所有信息
    # 输出元组，包括option的key和value
    def get_section_all(self, section):
        self.__read_ini_file()
        return self.config.items(section)

    # 判断 section 是否存在  存在 True  不存在 False
    def judge_section(self, section):
        self.__read_ini_file()
        return section in self.config

    # 判断 是否存在指定节的选项
    def judge_option(self, section, option):
        self.__read_ini_file()
        boolean = self.config.has_option(section, option)
        return boolean

    # 增  分组
    def add_section(self, section):
        self.__read_ini_file()
        self.config.add_section(section)
        self.__submit_operation()

    # 增  分组和内容  要判断 如果 option 内容存在则不添加
    def add_a_data(self, section, option, datas):
        self.__read_ini_file()
        if self.judge_section(section) == True:
            pass
        elif self.judge_section(section) == False:
            self.config.add_section(section)
        if self.judge_option(section, option) == False:
            self.config.set(section, option, datas)
            self.__submit_operation()
        elif self.judge_option(section, option) == True:
            print("[Warning] : already exist!")
        else:
            print("[Warning] : unusual!")

    # 删 section
    def del_section(self, section):
        self.__read_ini_file()
        self.config.remove_section(section)
        self.__submit_operation()

    # 删 del_option
    def del_option(self, section, option):
        self.__read_ini_file()
        self.config.remove_option(section, option)
        self.__submit_operation()

    # 改
    def update_init_data(self, section, option, datas):
        self.__read_ini_file()
        if self.judge_section(section) == True:
            if self.judge_option(section, option) == True:
                self.config.set(section, option, datas)
                self.__submit_operation()
            elif self.judge_option(section, option) == False:
                print("[Warning] : Not Find " + str(option))
            else:
                print("[Warning] : unusual!")
        elif self.judge_section(section) == False:
            print("[Warning] : Not Find " + str(section))

    # 查
    def select_init_data(self, datas):
        print('select_init_data')

    '''	
             # has_section(section)  # 是否存在该节
             boolean = config.has_section("mysql")

            boolean = config.has_option("mysql", "ip")  # 是否存在指定节的选项

            configparser.MAX_INTERPOLATION_DEPTH  # 使用默认插值时,  当raw=false，get()递归插值的最大深度

             config.clear()  # 所有节都包含'DEFAULT'值,对节的清空不会删除'DEFAULT'值
             config.BOOLEAN_STATES.update({'enabled': True, 'disabled': False})  # 自定义boolean的判断
             config.SECTCRE = re.compile(r"\[ *(?P<header>[^]]+?) *\]")  # 自定义节头的编译与解析的正则表达式(去除左右空格)

             config.read_file(open('config.ini', encoding="utf-8-sig"))
            # read_string(string, source='<string>')  # 从字符串解析配置数据
            config.read_string(config_str)
             # read_dict(dictionary, source='<dict>')  # 读取字典
             config.read_dict({'section1': {'key1': 'value1',
                                    'key2': 'value2'},
                       'section2': {'key3': 'value3',
                                   'key4': 'value4'}
     })'''