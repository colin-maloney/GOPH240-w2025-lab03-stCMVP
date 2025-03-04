import numpy as np 
import matplotlib.pyplot as plt 



def root_newton_raphson(x0, f, dfdx, tol=5e-6, max_iter=100): 
    """ 
    Parameters: 
    x0: float 
        Initial guess for the root 
    f: numpy.ndarray 
        Function to evaluate the root 
    dfdx: numpy.ndarray
        Derivative of the function f
    tol: float
        Tolerance for the root 
    max_iter: int
        Maximum number of iterations
    Returns: 
    x: float 
        The root of the function   
    """
    x = x0 

    for i in range(max_iter): 
       fx =f(x) 
       dfx = dfdx(x) 

       x_new = x - fx/dfx 

       if abs(x_new - x) < tol: 
            return x_new 
    raise ValueError(f"Root not found within {max_iter} iterations")