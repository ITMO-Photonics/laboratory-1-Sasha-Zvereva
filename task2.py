import timeit
import numpy as np
import scipy.optimize as optimize

import time

def f(x): 
    return np.cos(x)/(1.+x**2)

def fprime(x):
    return (-(x**2+1.)*np.sin(x)-2.*x*np.cos(x))/(x**2+1)**2


start_time = time.time()
brentq_x = optimize.brentq(f, 0.1, 2.4)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
bisect_x = optimize.bisect(f, 0.1, 2.4)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
newton_x = optimize.newton(f, 1.3)
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
newtonx2_x = optimize.newton(f, 1.3, fprime)
print("--- %s seconds ---" % (time.time() - start_time))
