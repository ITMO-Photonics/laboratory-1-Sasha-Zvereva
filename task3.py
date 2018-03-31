import numpy as np
import scipy.linalg as linalg

N=100
A=np.zeros((N,N))
i,j=np.indices((N,N))
A[i==j]=1
A[i==j+1]=1
A[i==j+2]=1
B=np.arange(N)
b=linalg.solve(A,B)
print(b)
