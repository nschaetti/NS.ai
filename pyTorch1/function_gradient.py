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
parser.add_argument(u"--iteration", type=int, required=True)

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

# Learning rate
learning_rate = 0.01

# Number of pass
n_iteration = 20

# Do 10 steps
for i in range(n_iteration):
    # Do backward pass
    if i != n_iteration - 1:
        z.backward(retain_graph=True)
    else:
        z.backward()
    # end if

    # For each parameters
    for p in parameters:
        p.data.sub_(p.grad.data * learning_rate)
    # end for

    # Print gradients and value
    print(u"x: {}, dz/dx: {}".format(x.data[0], x.grad[0][0]))
    print(u"y: {}, dz/dy: {}".format(y.data[0], y.grad[0][0]))
    print(u"")

    # Zero gradients
    x.grad.fill_(0)
    y.grad.fill_(0)
# end for
