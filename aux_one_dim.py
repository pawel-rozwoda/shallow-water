from numpy import sign
import numpy as np
from numpy import gradient

def extrapolate_in_time(u_old, u_new):
    return (u_old + u_new) * 1.5

def grad(mass):
    l = gradient(mass[0])
    l = list([l])
    return np.array(l)



def interpolate_in_space(uh, h):
    u = np.zeros((uh.shape[0], uh.shape[1] + 1))

    for i in range(uh.shape[1] - 1):
        u[0][i+1] = ( uh[0][i] + h[0][i]) / 2.

    return u 
