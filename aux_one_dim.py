from numpy import sign
import numpy as np
from numpy import gradient


#extrapolation to value^{t+0.5}
def extrapolate_in_time(u_old, u_new):
    return (3. * u_new - u_old) * .5


def grad(mass, dx=1.):
    return gradient(mass) / dx


def interpolate_in_space(uh, h):
    u = np.zeros((uh.shape[0] + 1))

    try:
        result = np.where(h > 0, uh/h, 0.)
#         result = np.where(h < 0 , 0, result)
    except:
        pass
    
    for i in range(1, u.shape[0] - 1):
        u[i] = (result[i-1] + result[i]) / 2.

    return u 
