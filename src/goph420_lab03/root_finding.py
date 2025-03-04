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
    for j, xj in enumerate(x): 
        x[j+1] = x[j] - f(x[j]) / dfdx(x[j])  
    if np.allclose(x[j+1], x[j]): 
        return x[j+1] 
    else:
        return ValueError("Root not found, try another initial guess") 
    
   
