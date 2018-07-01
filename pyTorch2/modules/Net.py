#!/usr/bin/env python
# -*- coding: utf-8 -*-
#


# Imports
import torch.nn as nn
import torch.nn.functional as F


# Neural net
class Net(nn.Module):
    """
    CNN
    """

    # Constructor
    def __init__(self):
        """
        Constuctor
        """
        super(Net, self).__init__()
        self.conv_layer1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 3)
        self.conv_layer2 = nn.Conv2d(6, 16, 5)
        self.linear_layer1 = nn.Linear(16 * 4 * 4, 120)
        self.linear_layer2 = nn.Linear(120, 10)
    # end __init__

    # Forward pass
    def forward(self, x):
        """
        Forward pass
        :param x:
        :return:
        """
        x = self.conv_layer1(x)
        x = F.relu(x)
        x = self.pool(x)
        x = self.conv_layer2(x)
        x = F.relu(x)
        x = self.pool(x)
        x = x.view(-1, 16 * 4 * 4)
        x = F.relu(self.linear_layer1(x))
        x = F.relu(self.linear_layer2(x))
        return x
    # end forward

# end Net
