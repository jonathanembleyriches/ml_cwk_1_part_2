import math

import numpy as np

def sigmoid(z):
    #########################################
    # Write your code here
    # modify this to return z passed through the sigmoid function
    return  1 / (1 + np.exp(-z))
    ########################################/
    
