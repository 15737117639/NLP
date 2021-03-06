# Rapid automatic keyword extraction(RAKE)

一般提取关键字的方法都是去掉停用词或者标点符号或者其他词汇意义很小的词。但是在人工提取关键字中，有些会包含停用词。
因此RAKE算法就没有删除停用词和短语分割符、词分割符。RAKE算法使用停用词和段落分割符来将文本预切割为一些候选关键字，
然后在这些候选关键字中使用滑动窗口(窗口大小默认为2)来确认词的联系(即词共现)。

## 候选关键字

RAKE先将文本按照一系列的词分割符分割成单词组，然后这些单词组会在短语分割符和停用词位置被分成一系列的毗邻词。
对于属于一系列的中词会被共同标记为候选关键字以及标记在文本中同一个位置。

候选关键字产生的步骤为：\
1、先用词分割符分割文本;\
2、再用停用词和短语分割词对分割好的字组再次进行分割。

## 关键字分数

在候选关键字确定和词共现图完成后，就要开始计算每个候选关键字的分数，候选关键字的分数为其包含的每个字的分数之和。
在计算关键字分数前，需要先介绍几个概念：\
1、字频\词频(freq(w)):字或者词在文章中出现的次数;\
2、字信度\词信度(deg(w)):字或者词在统一短语中共现的次数;\
3、信度与频率的比率(deg(w)/freq(w))\
那么该关键字的分数就是属于该词组中所有字或者短语的信度与频率的比率之和

在构成图模型的矩阵中，假如有N个字或者短语，图矩阵为NxN，对角线上填入该字或者短语的频率，其他位置写入对应词或者字共现的次数。

## 组合毗邻关键字
RAKE切分候选关键字有一部分是由停用词分割，但是RAKE认为对包含停用词的关键字也许更加具有说服力。因此，需要对毗邻的候选关键字进行重新组合。

组合毗邻关键字的标准是**这些关键字毗邻的次数在文本中要出现两次以上，并且其出现的次序还不能改变**，那么这些毗邻关键字才能合并。
新的候选关键字的分数为其包含的关键字的分数总和。

## 提取关键字
在对候选关键字打分后，进行排序，选择前T个候选关键字。本文T的值为在图中字或者词组数量的三分之一。


PS:\
1、我对网上给出有关RAKE的代码进行了修改，原来的代码在计算单个字的deg(即单个字的degree)的时候，并不是按照原文计算同一组短语中的词共现的次数，我将其修改过来了。\
2、我修改了部分代码，使其能够适合中文，由于中文需要分词的，单个词表示不了什么含义，所以我将分词后的词对应于英文中的单个单词。但是最后的结果还是不慎理想。


