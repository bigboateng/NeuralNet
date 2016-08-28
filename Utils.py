import numpy as np

class TransferFunctions:
    def __init__(self):
        self.params = None

    def LogisticRegression(self, t):
        return 1 / (1 + np.exp(-t))

    def LogisticRegressionPrime(self, z):
        return self.LogisticRegression(z) * (1 - self.LogisticRegression(z))


class Node:
    """
    :param tf = transfer function. Default = Logistic function
    """
    def __init__(self, tf=TransferFunctions.LogisticRegression):
        self.transfer_func = tf

class Layer:
    """
    @:param numOfNodes = Number of nodes in that layer
    """
    def __init__(self, nodes=None):
        self.nodes = nodes

    def get_nodes(self):
        return self.nodes

    def get_num_nodes(self):
        return len(self.nodes)