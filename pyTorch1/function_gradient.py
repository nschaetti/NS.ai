#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
#from __future__ import print_function
import torch
from torch.autograd import Variable
import argparse

# Arguments
parser = argparse.ArgumentParser(prog=u"function_gradient")
parser.add_argument(u"--learning-rate", type=float, required=True)
parser.add_argument(u"--iterations", type=int, required=True)
args = parser.parse_args()

# Create two variables
x = Variable(torch.ones(1), requires_grad=True)
y = Variable(torch.ones(1), requires_grad=True)

# Function to derive
z = 0.5*x*x + x + 0.25*y*y - 2

# Print gradients and value
print(u"x: {}".format(x.data[0]))
print(u"y: {}".format(y.data[0]))
print(u"z: {}".format(z.data[0]))

# List of parameters
parameters = list([x, y])

# List of positions
positions = list()

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
    positions.append((x.data[0], y.data[0]))
    """print(u"x: {}, dz/dx: {}".format(x.data[0], x.grad[0][0]))
    print(u"y: {}, dz/dy: {}".format(y.data[0], y.grad[0][0]))
    print(u"")"""

    # Zero gradients
    x.grad.fill_(0)
    y.grad.fill_(0)
# end for

print(u"Positions : {}".format(positions))
print(u"")
