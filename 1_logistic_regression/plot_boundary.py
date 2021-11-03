import numpy as np

def plot_boundary(X, theta, ax1):
    
    min_x1 = 0.0
    max_x1 = 0.0
    x2_on_min_x1 = 0.0
    x2_on_max_x1 = 0.0
    
    #########################################
    # Write your code here
    # Re-arrange the terms in the equation of the hypothesis function, and solve with respect to x2, to find its values on given values of x1
    x1_list = []
    for i in range(len(X)):
        x1_list.append(X[i][0])
    max_x1 = max(x1_list)
    i = x1_list.index(max_x1)
    min_x1 = min(x1_list)
    i2 = x1_list.index(min_x1)
    print("theta 1")
    print(X[i2][0] , theta[0], theta[1])
    x2_on_min_x1 = -(X[i][0]*theta[0])/theta[1]
    x2_on_max_x1 = -(X[i2][0]*theta[0])/theta[1]
    ########################################/
    
    x_array = np.array([min_x1, max_x1])
    y_array = np.array([x2_on_min_x1, x2_on_max_x1])
    ax1.plot(x_array, y_array, c='black', label='decision boundary')
    
    # add legend to the subplot
    ax1.legend()
