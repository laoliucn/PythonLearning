# code for a 3-layer neural network and code for learning the MNIST dataset

import numpy as np
# scipy.special for the sigmoid function expit()
import scipy.special
# lib for plotting arrays
import matplotlib.pyplot


# Neural network class definition
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden, output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # learning rate
        self.lr = learningrate

        # link weight metrics, wih and who
        # weights inside the arrays are w_i_j, where link is from node i to node j in the next layer
        # minus 0.5 to make some of the value is negative
        # self.wih = np.random.rand(self.hnodes, self.innodes) - 0.5
        # self.who = np.random.rand(self.onodes, self.hnodes) - 0.5

        # another init type, to use node link number平方根
        self.wih = np.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = np.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))

        # activation function is the sigmoid function
        self.activation_function = lambda x: scipy.special.expit(x)

    # train the neural network
    def train(self, input_list, target_list):
        # convert input list to 2d array
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(target_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # error is the (target - actual)
        output_errors = targets - final_outputs

        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = np.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * np.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                     np.transpose(hidden_outputs))
        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)), np.transpose(inputs))

    # query the neural network
    def query(self, inputs_lists):
        # convert inputs list to 2d array
        inputs = np.array(inputs_lists, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = np.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = np.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs


# number of input, hidden and output nodes
input_nodes = 784
hidden_nodes = 200
output_nodes = 10

# learning rate is 0.3
learning_rate = 0.2

# create instance of neural network
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# load the mnist training data CSV into a list
training_data_file = open('mnist_dataset/mnist_train.csv', 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# train the neural network
# go through all the records in the training data set
for record in training_data_list:
    # split the record by the ',' commas
    all_values = record.split(',')
    # scale and shift the inputs
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # create the target output values (all 0.01, except the desired label which is 0.99)
    targets = np.zeros(output_nodes) + 0.01
    targets[int(all_values[0])] = 0.99
    n.train(inputs, targets)

# test the neural network

# load the mnist test data CSV file into a list
test_data_file = open('mnist_dataset/mnist_test.csv', 'r')
test_data_list = test_data_file.readlines()
test_data_file.close()

# scorecard for how well the network performs, initially empty
scorecard = []

# go through all the records in the test data set
for record in test_data_list:
    # split the record by ','
    all_values = record.split(',')
    # target answer is the first value
    correct_label = int(all_values[0])
    # print('correct label is: ', correct_label)

    # scale and shift the inputs
    inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
    # query the network
    outputs = n.query(inputs)
    # got the index in array which has the biggest corresponding value
    label = np.argmax(outputs)
    # print("network's answer is: ", label)

    # append correct or incorrect to the list
    if label == correct_label:
        # network's answer matches correct answer, add 1 to the scorecard
        scorecard.append(1)
    else:
        # network's answer does not matches correct answer, add 0 to the scorecard
        scorecard.append(0)
print(scorecard)

# calculate the performance score, the fraction of correct answers
scorecard_array = np.asarray(scorecard)
print("Performance = ", scorecard_array.sum() / len(scorecard_array))

# image_array = np.asfarray(all_values[1:]).reshape((28, 28))
# matplotlib.pyplot.imshow(image_array, cmap='Greys', interpolation='None')
# matplotlib.pyplot.show()
# oresult = n.query((np.asfarray(all_values[1:])/255.0 * 0.99) + 0.01)
# print(oresult)
# print(np.argmax(oresult))
