import numpy as np 
import matplotlib.pyplot as plt 



def root_newton_raphson(x0, f, dfdx): 
    """ 
    Parameters: 
    x0: float 
        Initial guess for the root 
    f: numpy.ndarray 
        Function to evaluate the root 
    dfdx: numpy.ndarray
        Derivative of the function f
    Returns: 
    x: float 
        The root of the function   
    """
    x = x0
    tol = 5e-6 
    max_iter = 100 
    for i in range(max_iter): 
        x = x - f(x)/dfdx(x) 
        if np.abs(f(x)) < tol: 
            break