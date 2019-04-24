import numpy as np
import matplotlib.pyplot as plt
import math


def GMM(mean1, cov1, mean2, cov2, w1, w2, x, y):
    v1 = 1 / (2 * math.pi * cov1[0][0] * cov1[1][1] * math.sqrt(1 - cov1[1][0] ** 2))*math.exp(-1 / (2 * (1 - cov1[1][0] ** 2)) * (
                (x - mean1[0]) ** 2 / cov1[0][0] ** 2 + 2 * cov1[0][1] * (x - mean1[0]) * (y - mean1[1]) / (
                    mean1[0][0] * mean1[1][1]) + (y - mean1[1]) ** 2 / cov1[1][1] ** 2))
    v2 = 1 / (2 * math.pi * cov2[0][0] * cov2[1][1] * math.sqrt(1 - cov2[1][0] ** 2))*math.exp(-1 / (2 * (1 - cov2[1][0] ** 2)) * (
                (x - mean2[0]) ** 2 / cov2[0][0] ** 2 + 2 * cov2[0][1] * (x - mean2[0]) * (y - mean2[1]) / (
                    mean2[0][0] * mean2[1][1]) + (y - mean2[1]) ** 2 / cov2[1][1] ** 2))

    return w1*v1 +w2*v2





