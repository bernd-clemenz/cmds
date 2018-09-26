"""
Initialize the command executor module
(c) 2018 ISC Clemenz & Weinbrecht GmbH
"""
import configparser
import dateutil.parser
import logging
import logging.handlers
import os
import requests
import sys


name = 'cmds'

CFG = None
LOG = None


def init(config_name):
    global CFG, LOG, name
    
    # 1. check version and load configuration
    if sys.version_info.major < 3:
        raise Exception('Unsupported Python major version')
        
    if not os.path.isfile(config_name):
        raise Exception('config file missing')    

    CFG = configparser.ConfigParser()
    CFG.read(config_name)
    
    # 2. initialize logging
    LOG = logging.getLogger(name)
    lv_cfg = CFG[name]['log.level']
    lv_mp = {'INFO': logging.INFO,
             'WARN': logging.WARNING,
             'DEBUG': logging.DEBUG,
             'FATAL': logging.FATAL,
             'ERROR': logging.ERROR}
    if lv_cfg is not None and lv_cfg in lv_mp.keys():
        level = lv_mp[lv_cfg]
    else:
        level = logging.INFO

    LOG.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rh = logging.handlers.RotatingFileHandler(CFG[name]['log.file'],
                                              maxBytes=1024 * 1024,
                                              backupCount=50)
    ch = logging.StreamHandler()
    rh.setFormatter(formatter)
    ch.setFormatter(formatter)
    LOG.addHandler(rh)
    LOG.addHandler(ch)
    
    LOG.info(name + ' initialized.')