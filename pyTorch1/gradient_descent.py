#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import argparse
import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import axes3d, Axes3D
from matplotlib import cm


# Function
def func(xv, yv):
    """
    Function
    :param xv: X
    :param yv: Y
    :return: Z
    """
    return 0.5*math.pow(xv, 2) + xv + 0.25*math.pow(yv, 2) - 2
# end func


# Arguments
parser = argparse.ArgumentParser(prog=u"function_gradient")
parser.add_argument(u"--learning-rate", type=float, required=True)
parser.add_argument(u"--iterations", type=int, required=True)
parser.add_argument(u"--x", type=float, default=1.0)
parser.add_argument(u"--y", type=float, default=1.0)
args = parser.parse_args()

# Create two variables
x = args.x
y = args.y

# List of positions
x_values = list([x])
y_values = list([y])
z_values = list([func(x, y)])

# Do 10 steps
for i in range(args.iterations):
    # Compute gradient
    x_grad = x + 1
    y_grad = 0.5 * y

    # Update each parameters
    x -= x_grad * args.learning_rate
    y -= y_grad * args.learning_rate

    # Print gradients and value
    x_values.append(x)
    y_values.append(y)
    z_values.append(func(x, y))
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
        Z[j, i] = func(x_pos,y_pos)
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

# Show graph
plt.show()
