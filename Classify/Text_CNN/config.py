# coding:utf-8



def seq_param():
    import tensorflow as tf
    # 卷积的宽度，在cnn中，卷积的长度为词向量的长度，宽度表示包含多少词
    tf.flags.DEFINE_string('filter_size', '3,4,5', 'Comma-separated filter sizes (default: "3,4,5")')

    # 每种卷积的个数
    tf.flags.DEFINE_integer('filter_num', 128,  "Number of filters per filter size (default: 128)")

    # dropout概率
    tf.flags.DEFINE_float("dropout_prob",0.5,"Dropout keep probability (default: 0.5)")

    # 训练多少次后，进行验证
    tf.flags.DEFINE_integer("evaluate_every", 100, "evaluate model on dev set after many step (default: 100)")

    # 是否记录设备指派情况
    tf.flags.DEFINE_boolean("log_device_placement",False,"Log placement of ops on devices")

    # 是否自动选择运行设备
    tf.flags.DEFINE_boolean("allow_soft_placement",True,"Allow device soft device placement")

    # 限制gpu的使用率，如果满负荷运转，会造成其他资源无法调用gpu
    tf.flags.DEFINE_float('per_process_gpu_memory_fraction', 0.6, "limit gpu use,other could use gpu")

    # 模型和summary的输出文件夹
    tf.flags.DEFINE_string('out_dir', './', 'Output directory for model and summary')

    # 最多保存的中间结果
    tf.flags.DEFINE_integer("num_checkpoints",5,"Number of checkpoints to store (default: 5)")

    # 每块包含的数据量
    tf.flags.DEFINE_integer('batch_size',60,'num of each batch')

    # 训练轮数
    tf.flags.DEFINE_integer('num_epochs',200,'Number of training epochs (default: 200)')

    # 验证集的比例
    tf.flags.DEFINE_float('dev_sample_percent',0.01,'percentage of the train data to use for evaluate')

    # 语料库文件存放位置
    tf.flags.DEFINE_string('corpus_dir','../../Dataset/new_sohu.txt','where is corpus')

    FLAGS=tf.flags.FLAGS
    return FLAGS


import argparse
def Argparse():
    parser=argparse.ArgumentParser()
    # 卷积的宽度，在cnn中，卷积的长度为词向量的长度，宽度表示包含多少词
    parser.add_argument('--filter_size', default=[3,4,5], help='Comma-separated filter sizes (default: "3,4,5")',type=list)

    # 每种卷积的个数
    parser.add_argument('--filter_num', default=128,  help="Number of filters per filter size (default: 128)",type=int)

    # dropout概率
    parser.add_argument("--dropout_prob",default=0.5,help="Dropout keep probability (default: 0.5)",type=float)

    # 训练多少次后，进行验证
    parser.add_argument("--evaluate_every", default=100, help="evaluate model on dev set after many step (default: 100)",type=int)

    # 是否记录设备指派情况
    parser.add_argument("--log_device_placement",default=False,help="Log placement of ops on devices",type=bool)

    # 是否自动选择运行设备
    parser.add_argument("--allow_soft_placement",default=True,help="Allow device soft device placement",type=bool)

    # 限制gpu的使用率，如果满负荷运转，会造成其他资源无法调用gpu
    parser.add_argument('--per_process_gpu_memory_fraction', default=0.6, help="limit gpu use,other could use gpu",type=float)

    # 模型和summary的输出文件夹
    parser.add_argument('--out_dir', default='./', help='Output directory for model and summary',type=str)

    # 最多保存的中间结果
    parser.add_argument("--num_checkpoints",default=5,help="Number of checkpoints to store (default: 5)",type=int)

    # 每块包含的数据量
    parser.add_argument('--batch_size',default=1000,help='num of each batch',type=int)

    # 训练轮数
    parser.add_argument('--num_epochs',default=200,help='Number of training epochs (default: 200)',type=int)

    # 语句的最大长度
    parser.add_argument('--max_sequence_length',default=200,help='the max of one sequence',type=float)

    # 是否是在训练阶段
    parser.add_argument('--is_training',default=True,type=bool,help='whether is training this stage(default:True)')

    # 将处理过的文本保存的目标文件
    parser.add_argument('--target_file', default='../../Dataset/target_file.txt',help='After deal corpus txt ,where is save', type=str)

    # 这是存放验证数据的文件
    parser.add_argument('--valid_file',default='../../Dataset/valid_file.txt',help='this is a validation data file',type=str)

    # 这是存放训练数据的文件
    parser.add_argument('--train_file',default='../../Dataset/train_file.txt',help='this is a train data file',type=str)

    # 存放语料库词汇的文件
    parser.add_argument('--vocab_file',default='../../Dataset/vocab_file.txt',help='this is a vocabulary file',type=str)

    arg=parser.parse_args()
    return arg


import logging

def log_config(name):
    logger=logging.getLogger(name)
    logger.setLevel(logging.INFO)
    sh=logging.FileHandler('./log.log')
    fmt='%(asctime)s %(filename)s %(funcName)s %(lineno)s line %(levelname)s >>%(message)s'
    dtfmt='%Y %m %d %H:%M:%S'
    formatter=logging.Formatter(fmt=fmt,datefmt=dtfmt)
    sh.setFormatter(formatter)
    logger.addHandler(sh)
    return logger




