import numpy as np
import scipy as sci
from Activation import *
class Layer():
    def __init__(self, noOfUnitsInPrevLayer, noOfUnitsinLayer, activation):
        self.prevCount=noOfUnitsInPrevLayer
        self.curCount=noOfUnitsinLayer
        self.activation=activation
        self.weight=np.random.randn(noOfUnitsInPrevLayer,noOfUnitsinLayer)

    def forward(self, input):
        z=np.dot(input, self.weight)
        if self.activation=="sigmoid":
            return sigmoid(z)
        elif self.activation=="softmax":
            return softmax(z)
