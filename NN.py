import numpy as np
import random
from Utils import TransferFunctions

class NeuralNetwork:
    def __init__(self, inputLayer, outputLayer, hiddenLayers):
        self.inputLayer = inputLayer
        self.outputLayer = outputLayer
        self.hiddenLayers = hiddenLayers
        self.totalNumLayers = 2 + len(hiddenLayers)
        self.layers = [self.inputLayer]
        self.layers.extend(self.hiddenLayers)
        self.layers.append(self.outputLayer)
        #print(self.layers)
        # [ [1,1,2], [1,1]]
        self.weights = []
        #print("Number of Layers = {}".format(self.totalNumLayers))
        for i in range(self.totalNumLayers):
            if i < self.totalNumLayers - 1:
                w = np.random.rand(self.layers[i].get_num_nodes(), self.layers[i+1].get_num_nodes())
                #print("{}".format(w))
                self.weights.append(w)
        print(self.weights)



    def train(self, X, Y):
        print("gg")

    def forward(self, X):
        Y = X
        tf = TransferFunctions()
        for i in range(len(self.weights)):
            Y = np.dot(tf.LogisticRegression(Y), self.weights[i])

        print(Y)

