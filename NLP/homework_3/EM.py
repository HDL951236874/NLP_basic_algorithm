import numpy as np
import matplotlib.pyplot as plt
import math


def GM(mean, cov, x, y):
    # print(cov)
    v = 1 / (2 * math.pi * cov[0][0] * cov[1][1] * math.sqrt(1 - 0.5)) * math.exp(
        -1 / (2 * (1 - cov[1][0] ** 2)) * (
                (x - mean[0]) ** 2 / cov[0][0] ** 2 - 2 * cov[0][1] * (x - mean[0]) * (y - mean[1]) / (
                cov[0][0] * cov[1][1]) + (y - mean[1]) ** 2 / cov[1][1] ** 2))

    return v


def update(lx, ly, lr):
    new_m_1 = np.array([sum(lx * lr) / sum(lr), sum(ly * lr) / sum(lr)])
    new_m_2 = np.array([sum(lx * (1 - lr)) / sum((1 - lr)), sum(ly * (1 - lr)) / sum((1 - lr))])

    new_c_1 = np.array(
        [[sum(((lx - new_m_1[0]) ** 2) * lr) / sum(lr), sum((lx - new_m_1[0]) * (ly - new_m_1[1]) * lr) / sum(lr)],
         [sum((lx - new_m_1[0]) * (ly - new_m_1[1]) * lr) / sum(lr), sum(((ly - new_m_1[1]) ** 2) * lr) / sum(lr)]])

    new_c_2 = np.array(
        [[sum(((lx - new_m_2[0]) ** 2) * (1-lr)) / sum((1-lr)), sum((lx - new_m_2[0]) * (ly - new_m_1[1]) * (1-lr)) / sum((1-lr))],
         [sum((lx - new_m_2[0]) * (ly - new_m_1[1]) * (1-lr)) / sum((1-lr)), sum(((ly - new_m_2[1]) ** 2) * (1-lr)) / sum((1-lr))]])

    return new_m_1,new_m_2,new_c_1,new_c_2



def stop(new_m, old_m, new_cov, old_cov):
    m = abs(new_m - old_m)
    c = abs(new_cov - old_cov)
    if np.size(m[m > 0.000001]) == 0 and np.size(c[c > 0.000001]) == 0:
        return True
    else:
        return False


def run():
    mean1 = np.array([10, 10])
    cov1 = np.array([[2, 0], [0, 2]])
    mean2 = np.array([5, 5])
    cov2 = np.array([[1, 0], [0, 1]])

    num = 100

    l = np.vstack((np.random.multivariate_normal(mean1, cov1, num), np.random.multivariate_normal(mean2, cov2, num)))
    lx = l[:, 0]
    ly = l[:, 1]

    m_1 = np.array([9 + 2 * np.random.rand(), 9 + 2 * np.random.rand()])
    c_1 = np.array(
        [[1 + 2 * np.random.rand(), -1 + 2 * np.random.rand()], [-1 + 2 * np.random.rand(), 1 + 2 * np.random.rand()]])

    m_2 = np.array([4 + 2 * np.random.rand(), 4 + 2 * np.random.rand()])
    c_2 = np.array(
        [[2 * np.random.rand(), -1 + 2 * np.random.rand()], [2 * np.random.rand(), -1 + 2 * np.random.rand()]])

    print(m_1)
    print(c_1)
    print(m_2)
    print(c_2)

    lr = []

    flag = False
    while not flag:
        lr = []

        for i in range(2 * num):
            r = GM(m_1, c_1, lx[i], ly[i]) / (GM(m_2, c_2, lx[i], ly[i]) + GM(m_1, c_1, lx[i], ly[i]))
            lr.append(r)

        lr = np.array(lr)

        n_m_1, n_m_2, n_c_1, n_c_2 = update(lx, ly, lr)

        flag_1 = stop(n_m_1, m_1, n_c_1, c_1)
        flag_2 = stop(n_m_2, m_2, n_c_2, c_2)

        flag = flag_1 and flag_2
        # print(flag)

        m_1, c_1, m_2, c_2 = n_m_1, n_c_1, n_m_2, n_c_2

    print(m_1)
    print(c_1)
    print(m_2)
    print(c_2)


if __name__ == '__main__':
    run()
    # mean1 = np.array([5, 5])
    # cov1 = np.array([[2, 0], [0, 2]])
    # mean2 = np.array([0, 0])
    # cov2 = np.array([[1, 0], [0, 1]])
    # print(GM(mean1,cov1,5,5))
    # print(GM(mean1,cov1,0.5,-0.5))






    # plt.scatter([x[0] for x in test1], [x[1] for x in test1])
    # plt.scatter([x[0] for x in test2], [x[1] for x in test2])
    #
    # plt.show()
