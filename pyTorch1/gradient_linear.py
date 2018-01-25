#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import argparse
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import cm
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim

# Random seed
torch.manual_seed(1)
np.random.seed(1)

# True parameter values
a = 4
c = 2

# Noise parameter
v = 8

# Number of samples
n_samples = 50

# Generate samples
X = np.zeros(n_samples)
Y = np.zeros(n_samples)
for i in range(n_samples):
    x = np.random.rand()*10.0
    y = a*x + c + 5*(2*np.random.rand()-1.0)
    X[i] = x
    Y[i] = y
# end for

# Variable x
# x = Variable(torch.ones(1), requires_grad=True)

# Linear layer
linear = nn.Linear(1, 1, bias=True)
linear.cuda()

# Test sample
"""x_target = 4
x_target = Variable(torch.Tensor(1).fill_(x_target))
y_target = a * 4 + c
y_target = Variable(torch.Tensor(1).fill_(y_target))

# Get output and compute loss with Mean Square Error
out = linear(x_target)
print(u"a : {}".format(list(linear.parameters())[0]))
print(u"c : {}".format(list(linear.parameters())[1]))
print(u"Inputs : {}".format(x_target))
print(u"Outputs : {}".format(out))
print(u"Target : {}".format(y_target))"""

# Objective function is Mean Squared Error
criterion = nn.MSELoss()

# Compute loss
"""loss = criterion(out, y_target)
print(u"Loss : {}".format(loss))

# Gradient
print(loss.grad_fn)
print(loss.grad_fn.next_functions[0][0])
print(loss.grad_fn.next_functions[0][0].next_functions[0][0])
print(loss.grad_fn.next_functions[0][0].next_functions[0][0].next_functions[0][0])"""

# Learning parameters
learning_parameters = 0.01

""""# Backprop
linear.zero_grad()
print(u"a grad befpre backward : {}".format(list(linear.parameters())[0].grad))
print(u"c grad before backward : {}".format(linear.bias.grad))
loss.backward()
print(u"a grad before backward : {}".format(list(linear.parameters())[0].grad))
print(u"c grad after backward : {}".format(linear.bias.grad))"""

# Optimizer
optimizer = optim.SGD(linear.parameters(), lr=learning_parameters)

# Loop over the data set
for epoch in range(500):
    # Inputs and outputs (n_samples * in_features)
    inputs, outputs = torch.Tensor(X).unsqueeze(1), torch.Tensor(Y).unsqueeze(1)

    # To variable
    inputs, outputs = Variable(inputs.cuda()), Variable(outputs.cuda())

    # Zero param gradients
    optimizer.zero_grad()

    # Forward + Backward + optimize
    linear_outputs = linear(inputs)
    loss = criterion(linear_outputs, outputs)
    loss.backward()
    optimizer.step()

    # Print result
    if epoch % 10 == 0:
        print(u"Loss {} : {}".format(epoch, loss.data[0]))
    # end if
# end for

# Get and print parameter
model_a = float(list(linear.parameters())[0])
model_c = float(linear.bias)
print(u"Found a : {}".format(model_a))
print(u"Found c : {}".format(model_c))

# Show points and line
plt.scatter(X, Y, c='r', marker='o', s=1)
plt.plot([0, 10], [c, a * 10 + c], c='b')
plt.plot([0, 10], [model_c, model_a * 10 + model_c], c='g')
plt.show()
