import matplotlib.pyplot as plt
import os
import numpy as np


def main():
    data = np.loadtxt(os.path.join('data.txt'), delimiter=',')
    X, y = data[:, 0], data[:, 1]
    m = y.size
    # drawData(X, y)
    print(X)
    X = np.stack([np.ones(m), X], axis=1)
    print(X)


def computeCost(X, y, tetha):
    j = 0
    m = y.size
    number_features = tetha.size


    return j

def drawData(x, y):
    plt.plot(x, y, 'ro', ms=10, mec='k')
    plt.ylabel('Profit in $10,000')
    plt.xlabel('Population of City in 10,000s')
    plt.show()


if __name__ == "__main__":
    main()
