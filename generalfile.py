
# -*- coding=utf-8 -*-
__author__ = '-ling'


import os
import sys
import time
import json
import shutil
import configparser


class Gen_File_handle():
    '''
            对文件操作的类;
            @ file_path : 文件路径；
    '''

    def __init__(self, file_path):
        self.file_path = file_path

    #	读取文件所有内容
    def read_all_data(self):
        """ 一次读取整个文件 """
        with open(self.file_path, mode='r', encoding='utf-8') as f:
            return f.read()

    """ 按行读取，去掉行尾换行符 """
    def read_file_by_line(file):
        with open(file, mode='r', encoding='utf-8') as f:
            while True:
                one_line = f.readline()
                if not one_line:
                    return
                else:
                    yield one_line.strip()  # 去掉每行结尾的换行

    """ 按行读取，遇到空行退出 """
    def read_file_by_line_blank(file):

        with open(file, mode='r', encoding='utf-8') as f:
            while True:
                one_line = f.readline().strip()
                if not one_line:
                    return
                yield one_line


    """ 按行读取，跳过以startwith开头的行，遇到空行退出 """
    def read_file_by_line_skip(file, startwith=None):
        with open(file, mode='r', encoding='utf-8') as f:
            while True:
                one_line = f.readline().strip()
                while one_line.startswith(startwith):
                    one_line = f.readline().strip()
                if not one_line:
                    return
                yield one_line

    # lines = read_file_by_line('test.txt')
    # for line in lines:
    #     print(line)
    #
    # lines = read_file_by_line_skip('test.txt', startwith='#')
    # for line in lines:
    #     print(line)

    """ 按块读取 """

    def read_file_by_chunk(file, chunk_size=512):
        with open(file, mode='r', encoding='utf-8') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    return
                yield chunk

    # chunks = read_file_by_chunk('test.txt')
    # for chunk in chunks:
    #     print(chunk, end='')



    #	检查文件是否存在
    def examine_file(self):
        # return os.path.exists(self.file_path)
        if os.path.exists(self.file_path) == False:
            print("文件不存在")
            return "NotFile"
        else:
            return True

    #	写入文件
    #	@datas : 要写入文件的内容
    def write_one_data(self, datas):
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            print(type(datas))
            input_data = str(datas)
            print(type(input_data))
            file.write(input_data + "\n")

    #	对文件写入所有数据
    #	@ data_list : 要写入文件的所有内容
    def write_file_all(self, data_list):
        with open(self.file_path, 'w+', encoding='utf-8') as file:
            for file_data in data_list:
                file.write(file_data)

    # 普通的写入文件
    def write_datas(self, datas):
        with open(self.file_path, 'w+', encoding='utf-8') as file:
            file.write(datas)

    #	文件添加一行内容
    # 	@datas : 要写入文件的内容
    def add_data(self, datas):
        with open(self.file_path, 'a+', encoding='utf-8') as file:
            input_data = str(datas)
            file.write(input_data + "\n")

    #	获取文件总行数
    def get_file_data_len(self):
        file_all_datas = self.read_all_data()
        if file_all_datas != 'NotFile':
            print(len(file_all_datas))
            return len(file_all_datas)

    #	读取文件指定行数
    # 	@len_number : 指定行数
    def get_file_line_data(self, len_number):
        data_cont = 0
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                if (data_cont == (len_number - 1)):
                    print(data_cont)
                    # print(str(line).encode('gb2312'))
                    print(type(line))
                    return line
                data_cont += 1
            else:
                print("not find file len Min = 1 ; Max = " + str(data_cont))

    #	修改指定行内容
    # 	@len_number : 指定行数
    # 	@datas : 要写入文件的内容
    def modif_file_line_data(self, len_number, datas):
        input_data = str(datas)
        input_data = input_data.replace("\'", "\"")
        file_all_datas = self.read_all_data()
        if file_all_datas != 'NotFile':
            # 修改方法
            file_all_datas[(len_number - 1)] = input_data + "\n"
            with open(self.file_path, 'w+', encoding='utf-8') as file:
                for file_data in file_all_datas:
                    file.write(file_data)

    # 在指定行插入内容
    def add_file_line_data(self, len_number, datas):
        input_data = str(datas)
        input_data = input_data.replace("\'", "\"")
        file_all_datas = self.read_all_data()
        if file_all_datas != 'NotFile':
            # 插入方法
            file_all_datas.insert((len_number - 1), input_data + "\n")
            self.write_file_all(file_all_datas)

    # 删除指定行
    def del_dile_line_data(self, len_number):
        file_all_datas = self.read_all_data()
        if file_all_datas != 'NotFile':
            # 删除方法
            del file_all_datas[(len_number - 1)]
            self.write_file_all(file_all_datas)

    # 清楚空，回车，空格，
    def clear_empty(self):
        file_all_datas = self.read_all_data()
        if file_all_datas != 'NotFile':
            # print(file_all_datas)
            file_all_datas = [x for x in file_all_datas if x != '\n' and x != '']
            # 删除 存在多个空格的情况
            kongge = " "
            kongge_number = 0
            while kongge_number < 10:
                str_pipei = kongge * kongge_number + "\n"
                if str_pipei in file_all_datas:
                    file_all_datas.remove(str_pipei)
                else:
                    kongge_number += 1
            self.write_file_all(file_all_datas)

    # 寻找内容在第几行,并返回
    def find_str_coordinate(self, datas):
        find_info = []
        rest = []
        data_cont = 1
        with open(self.file_path, 'r', encoding='utf-8') as file:
            for line in file:
                # line.encoding='gbk'
                if (datas in line):
                    find_info.append(data_cont)
                    rest.append(line)
                data_cont += 1
        if len(find_info) > 0:
            dic_rest = dict(map(lambda x, y: [x, y], find_info, rest))
            return dic_rest
        else:
            print("not find " + str(datas) + " from file.")

    # 获取文件属性
    def get_file_attribute_list(self):
        if self.examine_file() == True:
            '''
            st_mode: inode 保护模式
                -File mode: file type and file mode bits (permissions).
            st_ino: inode 节点号。
                -Platform dependent, but if non-zero, uniquely identifies the file for a given value of st_dev.
                ——the inode number on Unix,
                ——the file index on Windows
            st_dev: inode 驻留的设备。
                -Identifier of the device on which this file resides.
            st_nlink:inode 的链接数。
                -Number of hard links.
            st_uid: 所有者的用户ID。
                -User identifier of the file owner.
            st_gid: 所有者的组ID。
                -Group identifier of the file owner.
            st_size:普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
                -Size of the file in bytes, if it is a regular file or a symbolic link. The size of a symbolic link is the length of the pathname it contains, without a terminating null byte.
            st_atime: 上次访问的时间。
                -Time of most recent access expressed in seconds.
            st_mtime: 最后一次修改的时间。
                -Time of most recent content modification expressed in seconds.
            st_ctime:由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。
            st_atime_ns
                -Time of most recent access expressed in nanoseconds as an integer
            st_mtime_ns
                -Time of most recent content modification expressed in nanoseconds as an integer.
            st_ctime_ns
                -Platform dependent:
                    ——the time of most recent metadata change on Unix,
                    ——the time of creation on Windows, expressed in nanoseconds as an integer.
            --------------------- 
            '''
            attribute_list = os.stat(self.file_path)
            print(attribute_list)
            # 查看文件的修改时间
            file_modif_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(attribute_list.st_mtime))
            print("文件的修改时间 : " + file_modif_time)
            # 查看文件的上次访问时间
            file_access_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(attribute_list.st_atime))
            print("文件的上次访问时间 : " + file_access_time)
            # 文件大小
            file_size = attribute_list.st_size / 1024
            print("文件大小 : " + str(file_size) + "KB")
            file_attribute_rest = {"file_size": file_size, "file_modif_time": file_modif_time,
                                   "file_access_time": file_access_time}
            return file_attribute_rest

    # 获取文件所在目录
    def get_file_dir(self):
        # print(os.path.abspath(self.file_path))
        # print(os.path.dirname(os.path.abspath(self.file_path)))
        return os.path.dirname(os.path.abspath(self.file_path))

    # 复制文件
    def copy_file(self, targetDir):
        if self.examine_file() == True:
            input_file = str(self.get_file_dir())
            targetDir_list = targetDir.split("/")
            # 如果目录存在这个文件 则从命名
            if targetDir_list == input_file.split("\\"):
                # print(targetDir+" have file")
                file_new_name = self.file_path.split(".")[0] + "_mancopy." + self.file_path.split(".")[1]
                print(file_new_name)
                shutil.copy(self.file_path, file_new_name)
            else:
                # print("copy file")
                shutil.copy(self.file_path, targetDir)

    # 删除文件
    def del_file(self):
        if self.examine_file() == True:
            os.remove(self.file_path)

    # 移动文件
    def move_file(self, dstfile):
        if self.examine_file() == True:
            input_file = str(self.get_file_dir())
            dstfile_list = dstfile.split("/")
            if dstfile_list == input_file.split("\\"):
                pass
            else:
                shutil.move(self.file_path, dstfile)
