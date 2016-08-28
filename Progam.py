from Utils import TransferFunctions
from NN import NeuralNetwork
from Utils import *
if __name__ == "__main__":
    # input Layer
    inputNode1 = Node(tf=None)
    inputNode2 = Node(tf=None)
    inputLayer = Layer([inputNode1, inputNode2])

    # output layer
    output_node = Layer(TransferFunctions.LogisticRegression)
    outputLayer = Layer([output_node])

    # hidden layer
    hiddenLayer1 = Layer([Node(TransferFunctions.LogisticRegression) for i in range(4)])
    hiddenLayer2 = Layer([Node(TransferFunctions.LogisticRegression) for i in range(4)])
    hiddenLayers = [hiddenLayer1, hiddenLayer2]

    # data set example
    x_data = [[1,3], [3,2],[3,3],[4,5]]
    y_data = [(0), (0), (0), (1)]

    # NN setup

    # simple 1-2-1 NN
    startLayer = Layer([TransferFunctions.LogisticRegression])
    endLayer = Layer([TransferFunctions.LogisticRegression])
    hiddenLLayer = [Layer([TransferFunctions.LogisticRegression, TransferFunctions.LogisticRegression])]
    smallNN = NeuralNetwork(startLayer, endLayer, hiddenLLayer)
    #
    X = [1,2,4,5]
    x_vector = np.array([[1,2],
                         [3,4],
                         [5,6]])
    #smallNN.forward(x_vector)
    #print(x_vector)
    #nn = NeuralNetwork(inputLayer, outputLayer, hiddenLayers)
    #nn.train(x_data, y_data)
    #print(np.array([x_data]).T)
    a = np.array([X])
    smallNN.forward(a.T)
    #smallNN.forward(a)
        #nn.forward(np.arr)