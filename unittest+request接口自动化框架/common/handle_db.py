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
import pymysql
from common import handle_conf


class DB:
    def __init__(self, port, user, password, host):
        self.con = pymysql.connect(port=port,
                                   user=user,
                                   password=password,
                                   host=host,
                                   charset="utf8",
                                   cursorclass=pymysql.cursors.DictCursor)
        self.cur = self.con.cursor()

    def find_data(self, sql):
        self.con.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data


database_info = DB(port=eval(handle_conf.Conf.get("mysql", "port")),
                   user=handle_conf.Conf.get("mysql", "user"),
                   password=handle_conf.Conf.get("mysql", "password"),
                   host=handle_conf.Conf.get("mysql", "host"))
