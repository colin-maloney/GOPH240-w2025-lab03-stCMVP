import numpy as np 
import matplotlib.pyplot as plt 
from goph420_lab03.root_finding import root_newton_raphson 

def Fx(x): 
    return x**2 -1 
def dFx(x): 
    return 2*x 

root_newton_raphson(1, Fx, dFx) 
# Call the function 
result = root_newton_raphson(1, Fx, dFx) 
print(result)