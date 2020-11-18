'''
    we want to predict a patienent of diabetis from this example data listed in data.csv

'''

import numpy as np
import pandas as pd

def sigmoid(n):
    return 1 / (1 + np.exp(-n))

def sigmoid_derivative(n):
    return sigmoid(n) * (1.0 - sigmoid(n))

def train_network(features, label, weights, bias, learning_rate, epochs):

    deriva_product = []

    for epoch in range(epochs):

    #loss = 1

    #while loss > 0:
        dot_product = np.dot(features, weights) + bias

        preds = sigmoid(dot_product)

        errors = preds - label

        deriva_cost_function = errors
        deriva_preds = sigmoid_derivative(preds)
        deriva_product = deriva_cost_function * deriva_preds
        features_T = features.T

        weights = weights - np.dot(features_T, deriva_product) * learning_rate

        loss = errors.sum()
        print(loss)

    for i in deriva_product:
        bias = bias -  i * learning_rate

    return weights, bias
    

df = pd.read_csv('/Users/renato.cacho/Documents/python-test/neural_network/data.csv')
#print(df.head())

# separating the features and label
x = df[['Glucose', 'BloodPresure']]
y = df['Diabetes']
         
np.random.seed(10)

features = x
label = y.values.reshape(y.shape[0],1)
#print(features)

weights = np.random.rand(2,1)
bias = np.random.rand(1)
learning_rate = 0.0000004
epochs = 100

weights_final, bias_final = train_network(features, label, weights, bias, learning_rate, epochs)


def test_value(glucose, blood_presure):
    inputs = [[77,105]]
    dot_prod = np.dot(inputs, weights_final) + bias_final
    preds = sigmoid(dot_prod) >= 1/2
    return preds[0][0]


'''

86,104,1
78,111,0
79,114,0
77,105,0
90,100,1

'''


result = test_value(86,104)
assert result == True, result

result = test_value(90,100)
assert result == True, result

result = test_value(78,111)
assert result == False, result

result = test_value(79,114)
assert result == False, result

result = test_value(77,105)
assert result == False, result

