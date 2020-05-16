from numpy import sign
import numpy as np
from numpy import gradient

#extrapolation to value^{t+0.5}
def extrapolate_in_time(u_old, u_new):
    return (u_new + u_old) * .5

def grad(mass):
    return gradient(mass)



def interpolate_in_space(uh, h):
    u = np.zeros((uh.shape[0] + 1))
    result = uh/h

    for i in range(1, u.shape[0] - 1):
        u[i] = (result[i-1] + result[i]) / 2.

    return u 
