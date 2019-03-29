import jieba
import csv
import re
import math

def cleantxt(raw):
    fil = re.compile(u'[^\u4e00-\u9fa5]+', re.UNICODE)
    return fil.sub(' ', raw)

def renmin():
    data = []
    csv_reader = csv.reader(open('人民日报98.txt', mode='r', encoding='utf-8'))
    for index in csv_reader:
        if len(index) == 0:
            continue
        else:
            data.append(cleantxt(index[0]).split(' ')[1:-1])

    word_dic = {}
    for n in data:
        for m in n:
            if m not in word_dic:
                word_dic[m] = 1
            else:
                word_dic[m] +=1

    res = sorted(word_dic.items(), key=lambda x: x[1], reverse=True)
    L = sum([x[1] for x in res])
    E = 0

    for n in res:
        E += math.log(L/n[1],2)*n[1]/L

    print(E)


def doupo():
    data_1 = []
    csv_reader = csv.reader(open('斗破苍穹.txt',mode='r',encoding='utf-8'))
    for index in csv_reader:
        if len(index) == 0:
            continue
        else:
            Str = cleantxt(index[0]).split(' ')

            if '' in Str:
                Str.remove('')

            if Str == ['']:
               continue

            for n in Str:
                if len(n) == 0:
                    Str.remove(n)
            # print(len(Str[-1]))


            data_1.append(Str)


    word_dic_1 = {}
    for n in data_1:
        for m in n:
            for l in jieba.cut(m,cut_all=False,HMM=True):
                if l not in word_dic_1:
                    word_dic_1[l] = 1
                else:
                    word_dic_1[l] +=1

    res_1 = sorted(word_dic_1.items(), key=lambda x: x[1], reverse=True)
    L_1 = sum([x[1] for x in res_1])
    E_1 = 0

    for n in res_1:
        E_1 += math.log(L_1/n[1],2)*n[1]/L_1



    print(E_1)

def duihua():
    data_2 = []
    csv_reader = csv.reader(open('smsCorpus_zh_2015.03.09.xml',mode='r', encoding='utf-8'))
    for n in csv_reader:
        if len(n) == 0:
            continue
        else:
            pattern = re.compile('<city>.*</city>')
            x = re.sub(pattern,'',n[0])
            Str = cleantxt(x).split(' ')

            if '' in Str:
                Str.remove('')

            if Str == ['']:
               continue

            for n in Str:
                if len(n) == 0:
                    Str.remove(n)


            data_2.append(Str)

    word_dic_2 = {}
    for n in data_2:
        for m in n:
            for l in jieba.cut(m,cut_all=False,HMM=True):
                if l not in word_dic_2:
                    word_dic_2[l] = 1
                else:
                    word_dic_2[l] +=1

    res_2 = sorted(word_dic_2.items(), key=lambda x: x[1], reverse=True)
    L_2 = sum([x[1] for x in res_2])
    E_2 = 0

    for n in res_2:
        E_2 += math.log(L_2/n[1],2)*n[1]/L_2

    print(E_2)



if __name__ == '__main__':
    renmin()
    doupo()
    duihua()
