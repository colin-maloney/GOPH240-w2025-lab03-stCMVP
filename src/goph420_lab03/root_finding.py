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
    eps_a = 1.0 
    iter = 0 
    while eps_a > tol and iter < max_iter: 
        dx = -f(x)/dfdx(x)
        x += dx 
        eps_a = np.abs(dx/x) 
        iter += 1
        
    if iter >= max_iter and eps_a > tol:
        print(f"{iter} iterations completed with a relative error of {eps_a}") 
    return x