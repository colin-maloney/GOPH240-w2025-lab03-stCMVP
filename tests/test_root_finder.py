from goph420_lab03.root_finding import root_newton_raphson

def Fx(x):
    return x**2 -1
def dFx(x):
    return 2*x

root_newton_raphson(1, Fx, dFx)
# Call the function
result, iter, error = root_newton_raphson(1, Fx, dFx)
print("="*40)
print(f"Root: {result:.6}")
print(f"Iteration: {iter}")
print(f"Rel. Error: {error}")
print("="*40)