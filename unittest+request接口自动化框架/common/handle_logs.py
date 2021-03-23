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
import logging
from common import handle_path
from common import handle_conf
from logging.handlers import RotatingFileHandler
import os


def creat_log():
    log = logging.getLogger("Alem")
    log.setLevel(handle_conf.Conf.get("logging", "log_level"))

    fh = RotatingFileHandler(os.path.join(handle_path.LOG_PATH, handle_conf.Conf.get("logging", "fh_name")), mode="a",
                             maxBytes=1024 * 1024 * 10, backupCount=5, encoding="utf8")
    fh.setLevel(handle_conf.Conf.get("logging", "fh_level"))

    log.addHandler(fh)

    mate = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')

    fh.setFormatter(mate)

    return log


log = creat_log()
