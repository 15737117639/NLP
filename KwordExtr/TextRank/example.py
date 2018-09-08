#-*- encoding:utf-8 -*-

import codecs
from TextRankKeyword import TextRankKeyword
from TextRankSentence import TextRankSentence

# text = codecs.open('../test/doc/01.txt', 'r', 'utf-8').read()
tr4w = TextRankKeyword()
text = """据路透社9月6日报道称，两名消息人士向路透社透露称，一艘英国皇家海军的军舰在前往越南的路途中靠近中国南海海域的岛礁行驶，这被认为是英国皇家海军主张“航行自由”权利。文章称，几天前载有皇家海军陆战队员的排水量22000吨的海神之子号两栖舰从西沙群岛经过，这艘军舰当时行驶的目标是越南的胡志明市。在完成了在日本周边地区的部署后，从本周一开始它停靠在那里。消息人士称，当时北京派出一艘护卫舰和两架直升机对英国船只进行监控，但双方在遭遇期间保持冷静。另一个消息来源透露，海神之子号两栖舰并没有进入西沙群岛任何岛礁的12海里领海。路透社称，英国皇家海军发言人说：“海神之子号两栖舰在完全符合国际法和规范的情况下行使了航行自由权，”消息人士称，英国海军的军舰此前曾靠近南沙群岛的岛礁行驶，但没有进入岛礁12海里的领海范围内。
    　　在今年8月的中国国防部例行记者会上，国防部新闻发言人吴谦在接受采访时表示南海诸岛自古以来就是中国领土，这是一个事实。南海的航行自由没有问题，这是一个事实。南海行为准则磋商近期取得重大进展，这也是一个事实。一段时间以来，美方炒作南海问题，试图把影响航行自由的帽子扣在中方头上。我必须指出，谎言重复千遍也成为不了真理。
    　　注：英国海神之子级船坞登陆舰，于1998年5月23日由维克斯船舶工程公司开工建造，2001年3月9日下水，2003年6月19日服役。该舰满载排水量18400吨，舰长176米，宽28.9米。主要负责运送部队以及其武器、军备和一定数目的补给品作远征，抵达后使用登陆艇和直升机等工具，将部队和装备送上岸作战，亦可担任舰队旗舰，负责指挥整场两栖作战"""

tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象

print( '关键词：' )
for item in tr4w.get_keywords(20, word_min_len=1):
    print(item.word, item.weight)

print()
print( '关键短语：' )
for phrase in tr4w.get_keyphrases(keywords_num=20, min_occur_num= 2):
    print(phrase)

tr4s = TextRankSentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')

print()
print( '摘要：' )
for item in tr4s.get_key_sentences(num=3):
    print(item.index, item.weight, item.sentence)