import numpy as np
import matplotlib.pyplot as plt


# generate 100 points between -10 and 10.
input = np.linspace(-10,10,100)


def sigmoid(x):
    return 1/(1+np.exp(-x))


output = sigmoid(input)


plt.plot(input, output)
plt.xlabel('Input')
plt.ylabel('Output')
plt.title('Sogmoud function')

plt.show()