#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
from __future__ import print_function
import torch
from torch.autograd import Variable

# Create two variables
x = Variable(torch.ones(1), requires_grad=True)
y = Variable(torch.ones(1), requires_grad=True)

# Show
print(x)
print(y)

# Function to derive
z = 0.5*x*x + x + 0.25*y*y - 2

# Show
print(z, z.grad_fn)

# List of parameters
parameters = list([x, y])

# Learning rate
learning_rate = 0.01

# Do 10 steps
for i in range(10):
    # For each parameters
    for p in parameters:
        p.data.sub_(p.grad.data * learning_rate)
    # end for

    # Do backward pass
    if i != 9:
        z.backward(retain_graph=True)
    else:
        z.backward()
    # end if

    # Print gradients and value
    print(u"x: {}, dz/dx: {}".format(x.data[0], x.grad[0]))
    print(u"y: {}, dz/dy: {}".format(y.data[0], y.grad[0]))
    print(u"z: {}".format(z.data))
    print(u"")
# end for
