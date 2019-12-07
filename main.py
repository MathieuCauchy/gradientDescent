import os

import matplotlib.pyplot as plt
import numpy as np


def main():
    data = np.loadtxt(os.path.join('data.txt'), delimiter=',')
    X, y = data[:, 0], data[:, 1]
    m = y.size
    # drawData(X, y)
    X = np.stack([np.ones(m), X], axis=1)
    print(y)
    print(computeCost(X, y, np.array([2.0, 4.0])))


def computeCost(X, y, theta=np.array([0.0, 0.0])):

    h = (np.dot(X, theta.T) - y) ** 2
    print(np.dot(theta, X.T))
    return np.sum(h) / (2 * y.size)


def drawData(x, y):
    plt.plot(x, y, 'ro', ms=10, mec='k')
    plt.ylabel('Profit in $10,000')
    plt.xlabel('Population of City in 10,000s')
    plt.show()


if __name__ == "__main__":
    main()
