__author__ = 'himanshumisra'
import numpy as np
from NeuralNetwork import *

def main():
    X = np.array(([3,5], [5,1], [10,2]), dtype=float)
    y = np.array(([75], [82], [93]), dtype=float)
    X=X/np.amax(X, axis=0)
    y=y/100
    n=NeuralNetwork(X,y,[(3,"sigmoid")])
    print n.forward(X)
    print y

if __name__ == '__main__':
    main()