import numpy as np
def logistic_key(x, r, size):
    """
    This function accepts the initial x value, 
    r value and the number of keys required for
    encryption.
    The function returns a list of pseudo-random
    numbers generated from the logistic equation. 
    """

    key = []
    dt = 0.01

    # Initializing 3 empty lists
    xs = np.empty(size + 1, dtype = np.float64)
    ys = np.empty(size + 1, dtype = np.float64)
    zs = np.empty(size + 1, dtype = np.float64)

    # Initializing initial values
    # xs[0], ys[0], zs[0] = (xs, ys, zs)

    # Initializing constants
    s = 10
    xr = 28
    b = 2.667

    # System of equations
    for i in range(size):
        xs[i + 1] = xs[i] + (s * (ys[i] - xs[i]) * dt)
        ys[i + 1] = ys[i] + ((xs[i] * (r - zs[i]) - ys[i]) * dt)
        zs[i + 1] = zs[i] + ((xs[i] * ys[i] - b * zs[i]) * dt)
    
    for i in range(size):   
        x = r*x*(1-x)   # The logistic equation
        key.append(int((x*pow(10, 16))%256))    # Converting the generated number between 0 to 255

    return key