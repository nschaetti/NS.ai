#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

# Imports
import torch
from __future__ import print_function
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

# Compute gradient
z.backward(retain_graph=True)

# Print gradients
print(x.grad)
print(y.grad)

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
    print(x.data, x.grad)
    print(y.data, y.grad)
    print(z.data)
    print(u"")
# end for
