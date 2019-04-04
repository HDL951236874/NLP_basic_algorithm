import numpy as np
import csv

ls = ['abc',
      'brown',
      # 'chat80',
      # 'cmudict',
      'conll2000',
      'conll2002',
      'genesis',
      'gutenberg',
      # 'ieer',
      'inaugural',
      'indian',
      'names',
      # 'ppattach',
      # 'senseval',
      'shakespeare',
      'sinica_treebank',
      'state_union',
      'stopwords',
      # 'timit',
      'toolbox',
      'treebank',
      'udhr',
      'webtext',
      'words']

def spelling_detect(wor_A, wor_B):
    M = np.zeros((len(wor_A)+1,len(wor_B)+1))
    for i in range(len(wor_A)):
        M[i+1][0] = i+1
    for i in range(len(wor_B)):
        M[0][i+1] = i+1

    for n in range(1,M.shape[0]):
        for m in range(1,M.shape[1]):
            if wor_A[n-1] == wor_B[m-1]:
                M[n][m] = min(M[n-1][m-1], M[n-1][m]+1, M[n][m-1]+1)
            else:
                M[n][m] = min(M[n-1][m-1]+1, M[n-1][m]+1, M[n][m-1]+1)

    return M[-1][-1]


def diction():
    word_dic=[]
    csv_reader = csv.reader(open('dic.txt',mode='r'))
    for n in csv_reader:
        if len(n) == 0:
            continue
        word_dic.append([x.replace('\"','').replace(' ','') for x in n[0].split('\t')])

    W = {}
    for n in word_dic[1:]:
        for m in n:
            if len(m)==0 or not m.isalpha():
                continue
            if len(m) not in W:
                W[len(m)] = []
            if m not in W[len(m)]:
                W[len(m)].append(m)

    import pickle
    f = open('dic.dat',mode='wb')
    pickle.dump(W,f)


def Use_dic():
    import pickle
    fr = open('dic.dat',mode='rb')
    return pickle.load(fr)

def Use_misspelling():
    import pickle
    fr = open('misspelling.dat',mode='rb')
    return pickle.load(fr)

def Find_Surroundings(str, W):
    wrong_word = ''
    l = str.split(' ')
    '''find the wrong word'''
    for i in l:
        if i in W[len(i)]:
            continue
        else:
            wrong_word = i
            break

    w = []
    for i in W[len(wrong_word)-1]+W[len(wrong_word)]+W[len(wrong_word)]:
        if spelling_detect(wrong_word,i) == 1.0:
            w.append(i)

    return w,wrong_word

def choose_word_P1(w):

    num = 0
    for n in ls:
        for m in eval(n+'.fileids()'):
            comm = n+".words('"+m+"')"
            word = eval(comm)
            num += word.count(w)

    return num/8061333

def choose_word_P2(L,w,ww):
    try:
        if ww in L[w]:
            return float(1/len(L[w]))
        else:
            return float(1/len(L[w]))

    except:
        return 0.0


def misspelling():
    csv_reader = csv.reader(open('misspelling.txt',mode='r'))
    l = {}
    f = ''
    for n in csv_reader:
        if n[0][0] == '$':
            f = n[0][1:]
            l[f] = []
            continue
        l[f].append(n[0])

    import pickle
    f = open('misspelling.dat',mode='wb')
    pickle.dump(l,f)

def misspelling_2():
    csv_reader = csv.reader(open('misspelling_2.txt',mode='r'))
    l = {}
    for n in csv_reader:
        print(n)
        l[n[0].split(' ')[0][0:-1]] = [x for x in n[0].split(' ')[1:]] + n[1:]

    print(1)
    import pickle
    f = open('misspelling_2.dat',mode = 'wb')
    pickle.dump(l,f)



if __name__ == '__main__':
    # from nltk.corpus import *
    # W = Use_dic()
    # L = Use_misspelling()
    # l = []
    # w,ww = Find_Surroundings('acress',W)
    # w = list(set(w))
    # for n in w:
    #     p1 = choose_word_P1(n)
    #     p2 = choose_word_P2(L,n,ww)
    #     l.append(p1*p2)
    #
    # print(w[l.index(max(l))])


    misspelling_2()




