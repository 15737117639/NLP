# coding:utf-8
"""
全局配置
"""

import argparse

def argument():
    parser= argparse.ArgumentParser()

    # 语料库文件存放位置
    parser.add_argument('--corpus_txt',default='../Dataset/new_sohu.txt',help='where is corpus',type=str)

    # 测试语料库存放地址
    parser.add_argument('--test_txt',default='../Dataset/test.txt',help='where is test corpus',type=str)

    # 停用词语料库存放地址
    parser.add_argument('--stopfile',default='../Dataset/stopwords/stopwords.txt',help='stop words file',type=str)

    # 将处理过的文本保存的目标文件
    parser.add_argument('--target_file',default='../Dataset/target_file.txt',help='After deal corpus txt ,where is save',type=str)

    arg=parser.parse_args()
    return arg


import logging

def log_config():
    logger=logging.getLogger(__file__)
    logger.setLevel(logging.INFO)
    # sh=logging.FileHandler('./log.log')
    sh=logging.StreamHandler()
    fmt='%(asctime)s %(filename)s %(funcName)s %(lineno)s line %(levelname)s >>%(message)s'
    dtfmt='%Y-%m-%d %H:%M:%S'
    formatter=logging.Formatter(fmt=fmt,datefmt=dtfmt)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger