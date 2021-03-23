"""
========================================
# Author: Alem
# Email: chengrichong@foxmail.com  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Two roads diverged in a wood,and I 
# I took the one less traveled by, 
# And that has made all the difference. 
=========================================

"""
import os
from common import handle_path
import configparser


class Config(configparser.ConfigParser):

    def __init__(self, file_name, encoding="utf-8"):
        super().__init__()
        self.read(file_name, encoding=encoding)
        self.file_name = file_name
        self.encoding = encoding

    def write_data(self, select, option, value):
        """往配置文件中写数据"""
        self.set(select, option, value)
        self.write(fp=open(self.file_name, "w", encoding=self.encoding))


Conf = Config(os.path.join(handle_path.CONF_PATH, "config.ini"))
