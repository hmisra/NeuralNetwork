__author__ = 'himanshumisra'
import numpy as np
from Layer import *


class NeuralNetwork():
    def __init__(self, X,y, hiddenLayerConfiguration):
        self.X=X
        self.y=y
        self.layers=[]
        nsrc=X.shape[1]
        for each in hiddenLayerConfiguration:
            ndst=each[0]
            self.layers.append(Layer(nsrc, ndst, each[1]))
            nsrc=ndst
        self.layers.append(Layer(nsrc, y.shape[1], "sigmoid"))

    def train(self):
        a=0


    def forward(self, X):
        inp=X
        for each in self.layers:
            output=each.forward(inp)
            inp=output
        return inp





