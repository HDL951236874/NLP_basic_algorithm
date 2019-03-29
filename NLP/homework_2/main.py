import numpy as np
import csv

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
    # return M[-1][-1]


    # print(m)
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



    print(1)
    import pickle
    f = open('dic.dat',mode='wb')
    pickle.dump(W,f)


def Use_dic():
    import pickle
    fr = open('dic.dat',mode='rb')
    return pickle.load(fr)

def Find_Surroundings(str, W):
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

    return w





if __name__ == '__main__':
    W = Use_dic()

    print(Find_Surroundings('this is a godd day', W))




