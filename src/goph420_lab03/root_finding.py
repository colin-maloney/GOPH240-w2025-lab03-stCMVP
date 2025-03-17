import numpy as np

def root_newton_raphson(x0, f, dfdx, tol=5e-6, max_iter=100):
    """
    Parameters:
    x0: float
        Initial guess for the root
    f: function
        Function whose root is to be found
    dfdx: function
        Derivative of the function f
    tol: float
        Tolerance for the root
    max_iter: int
        Maximum number of iterations
    Returns:
    x: float
        The estimated root of the function
    iter: int
        Number of iterations taken
    error: np.ndarray
        Array of relative errors at each iteration
    """
    x = x0
    eps_a = 1.0  # Initial error
    iter = 0
    errors = []  # Store the errors at each iteration

    while eps_a > tol and iter < max_iter:
        dx = -f(x) / dfdx(x)
        x += dx
        eps_a = np.abs(dx / x)
        errors.append(eps_a)
        iter += 1

    if iter >= max_iter and eps_a > tol:
        print(f"Warning: {iter} iterations completed with a relative error of {eps_a}")

    return x, iter, np.array(errors)
