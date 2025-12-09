# 1. Initialize Network and Data ###########################

# Initialize a network function - init random weight and bias values
def initialize_network(n_inputs, n_hidden, n_outputs):
    network = list()
    hidden_layer = [{'weights':[random() for i in range(n_inputs + 1)]} for i in range(n_hidden)]
    network.append(hidden_layer)
    output_layer = [{'weights':[random() for i in range(n_hidden + 1)]} for i in range(n_outputs)]
    network.append(output_layer)
    return network


# 2. Forward Propagation ####################################

# Calculate neuron activation (sum) for an input : sum(weight_i * input_i) + bias
def activate_sum(weights, inputs):
    activation = weights[-1]
    for i in range(len(weights)-1):
        activation += weights[i] * inputs[i]
    return activation

# Activation function - Sigmoid : output = 1 / (1 + e^(-sum))
from math import exp
def sigmoid_activation(activation):
    return 1.0 / (1.0 + exp(-activation))

# Forward propagate input to a network output
def forward_propagate(network, row_data):
    inputs = row_data
    for layer in network:
        new_inputs = []
        for neuron in layer:
            activation = activate_sum(neuron['weights'], inputs)
            print("Inputs : " + str(activation))
            neuron['output'] = sigmoid_activation(activation)
            print("Outputs : " + str(neuron['output']))
            new_inputs.append(neuron['output'])
        inputs = new_inputs
    return inputs


# 3. Back Propagate Error ################################

# Backpropagate error and store in neurons
# output_error = (expected - output) * transfer_derivative(output)
# hidden_error = (weight_k * error_j) * transfer_derivative(output)
# Calculate the derivative of an neuron output = output * (1.0 - output)

def transfer_derivative(output):
    return output * (1.0 - output)

def backward_propagate_error(network, expected):
    for i in reversed(range(len(network))):
        layer = network[i]
        errors = list()
        if i != len(network)-1:
            for j in range(len(layer)):
                error = 0.0
                for neuron in network[i + 1]:
                    error += (neuron['weights'][j] * neuron['delta'])
                errors.append(error)
        else:
            for j in range(len(layer)):
                neuron = layer[j]
                errors.append(expected[j] - neuron['output'])
        for j in range(len(layer)):
            neuron = layer[j]
            neuron['delta'] = errors[j] * transfer_derivative(neuron['output'])
            print("Error : " + str(neuron['delta']))
            

# 4. Update Network ###################################
# Update network weights with error
# weight = weight + learning_rate * error * input
# weight = weight + learning_rate * error
def update_weights(network, row, l_rate):
    for i in range(len(network)):
        inputs = row[:-1]
        if i != 0:
            inputs = [neuron['output'] for neuron in network[i - 1]]
        for neuron in network[i]:
            for j in range(len(inputs)): 
                neuron['weights'][j] += l_rate * neuron['delta'] * inputs[j]
                print(neuron['delta'], neuron['weights'][j])                
            neuron['weights'][-1] += l_rate * neuron['delta']
            print(neuron['delta'], neuron['weights'][-1])