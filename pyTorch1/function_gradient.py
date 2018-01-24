#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import torch
from torch.autograd import Variable
import argparse
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib import cm

# Arguments
parser = argparse.ArgumentParser(prog=u"function_gradient")
parser.add_argument(u"--learning-rate", type=float, required=True)
parser.add_argument(u"--iterations", type=int, required=True)
parser.add_argument(u"--x", type=float, default=1.0)
parser.add_argument(u"--y", type=float, default=1.0)
args = parser.parse_args()

# Create two variables
x = Variable(torch.zeros(1).fill_(args.x), requires_grad=True)
y = Variable(torch.zeros(1).fill_(args.y), requires_grad=True)

# Function to derive
z = torch.pow(x, 2).mul(0.5) + x + torch.pow(y, 2).mul(0.25) - 2

# List of parameters
parameters = list([x, y])

# List of positions
x_values = list([args.x])
y_values = list([args.y])
z_values = list([0.5*args.x**2 + x + 0.25*args.y**2 - 2])

# Do 10 steps
for i in range(args.iterations):
    # Do backward pass
    if i != args.iterations - 1:
        z.backward(retain_graph=True)
    else:
        z.backward()
    # end if

    # For each parameters
    for p in parameters:
        p.data.sub_(p.grad.data * args.learning_rate)
    # end for

    # Print gradients and value
    x_values.append(x.data[0])
    y_values.append(y.data[0])
    z_values.append(0.5*math.pow(x.data[0], 2) + x.data[0] + 0.25*math.pow(y.data[0], 2) - 2)

    # Zero gradients
    x.grad.fill_(0)
    y.grad.fill_(0)
# end for

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# X position
X = np.zeros((51, 51))
X[:, ] = np.arange(-2.5, 2.6, 0.1)

# Y position
Y = np.zeros((51, 51))
for i in range(51):
    Y[i, :] = X[0, i]
# end for

# Compute Z
Z = np.zeros((51, 51))
for j in range(51):
    for i in range(51):
        x_pos = X[j, i]
        y_pos = Y[j, i]
        Z[j, i] = 0.5*math.pow(x_pos, 2) + x_pos + 0.25*math.pow(y_pos, 2) - 2
    # end for
# end for

# Labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot a basic surface.
ax.plot_surface(X, Y, Z, cmap=cm.hot, linewidth=0, antialiased=True, alpha=1.0)

# Scatter points
ax.plot(x_values, y_values, z_values, label='Learning curve', color='lightblue')

plt.show()

