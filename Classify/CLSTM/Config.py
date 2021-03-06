# coding:utf-8

import argparse

def argument():
    parser= argparse.ArgumentParser()

    # 是否处于训练阶段
    parser.add_argument('--is_training',default=True,type=bool,help='whether is training (default:True)')

    # 是否使用lstm模型
    parser.add_argument('--is_lstm',default=True,type=bool,help='whether is use lstm model (default:True)')

    # 是否使用双向LSTM或者双向GRU模型
    parser.add_argument('--is_bidirectional',default=True,type=bool,help='whether is use bidirectional RNN model (default:True)')

    # 每轮训练的样本数量
    parser.add_argument('--batch_size',default=2000,type=int,help='the sample size of every batch train')

    # 训练数据集
    parser.add_argument('--train_file',default='../../Dataset/train_file.txt',type=str,help='This file is used to save the data that is trained model.')

    # 验证数据集
    parser.add_argument('--valid_file',default='../../Dataset/valid_file.txt',type=str,help='This file is used to save the data that is valided model')

    # 字汇表
    parser.add_argument('--vocab_file',default='../../Dataset/vocab_file.txt',type=str,help='This file is used to save the data that is vocabulary word')

    # 最大文本长度
    parser.add_argument('--max_sequence_length',default=300,type=int,help='the maximum length of a sentence')

    # num_epochs，循环次数
    parser.add_argument('--num_epochs',default=50,type=int,help='the Maximum number of epochs')

    parser.add_argument('--num_checkpoints',default=3,type=int,help='保存模型结果的数量')

    parser.add_argument('--out_dir',default='./',type=str,help='模型参数保存的路径')

    parser.add_argument('--evaluate_every',default=100,type=int,help='训练多少次后， 进行验证')

    cnn_parse=parser.add_argument_group('CNN argument','About CNN argument')
    # cnn模型dropout概率
    cnn_parse.add_argument('--cnn_dropout',default=0.5,help='dropout argument of CNN model')
    # cnn模型的embedding大小
    cnn_parse.add_argument('--cnn_embedding',default=500,type=int,help='embedding size of cnn model')
    # cnn模型的卷积核数量
    cnn_parse.add_argument('--cnn_filter_num',default=64,type=int,help='filter num of cnn model')
    # cnn模型卷积核大小，给定的list，是多个卷积核的大小
    cnn_parse.add_argument('--cnn_filter_size',default=[3,4,5],type=list,help='Comma-separated filter sizes (default: "3,4,5")')
    # cnn模型的学习率
    cnn_parse.add_argument('--learn_rate',default=0.98,type=int,help='learning rate of cnn model')


    lstm=parser.add_argument_group('LSTM','About LSTM argument')
    # lstm模型每层的隐藏单元数
    lstm.add_argument('--rnn_hidden_unite',default=128,type=int,help='hidden state cell number of lSTM model ')
    # lstm模型的dropout 概率
    lstm.add_argument('--lstm_dropout',default=0.6,type=int,help='dropout prob of LSTM model')
    # lstm模型的层数，
    lstm.add_argument('--lstm_layer_num',default=5,type=int,help='the layer number of lstm ')

    # 是否使用多层双向lstm
    lstm.add_argument('--multbilstm',default=True,type=bool,help='whether use multiple bilstm (default: False)')

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
