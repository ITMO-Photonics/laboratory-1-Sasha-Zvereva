import time
import numpy as np
import scipy.linalg

N=50
A = np.random.random((N,N))
k = np.arange(N)
for t in np.linspace(0,10,100):
        b=k/(1.+k*t)
x1 = scipy.linalg.solve(A,b)
print(x1)

lu = scipy.linalg.lu_factor(A)
for t in np.linspace(0,10,100):
        b=k/(1.+k*t)
x2 = scipy.linalg.lu_solve(lu,b)
print(x2)

A2 = scipy.linalg.inv(A)
for t in np.linspace(0,10,100):
        b=k/(1.+k*t)
x3 = np.dot(A2,b)
print(x3)

start_time = time.time()
for t in np.linspace(0,10,100):
	x1 = scipy.linalg.solve(A,b)
stop = time.time()-start_time
print(stop)

start_time = time.time()
lu = scipy.linalg.lu_factor(A)
for t in np.linspace(0,10,100):
	x2 = scipy.linalg.lu_solve(lu,b)
stop = time.time()-start_time
print(stop)

start_time = time.time()
A2 = scipy.linalg.inv(A)
for t in np.linspace(0,10,100):
	x3 = np.dot(A2,b)
stop = time.time()-start_time
print(stop)
