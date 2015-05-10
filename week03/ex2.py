### calculating four different voltage of the system ###

### the other three equations are: 3*V_3 -v_1 - v_4 - v_+ = 0
### , 4*v_4 - v_1 - v_2 - v_3 = 0 , 3*v_2 - v_1 - v_4 = 0 ###


import numpy as np
from numpy.linalg import solve

A = np.array( [[4 , -1 , -1 , -1],[-1 , 0 , 3 , -1],[-1 , -1 , -1 , 4],[-1 ,3 , 0 , -1]] , float )
v = np.array([5 , 5, 0,0], float)
N = len(v)

for m in range( N): # makes diagonal elements eqaul to one
    val = A[m , m]
    A[m, :] /= val
    v[m] /= val 
    for i in range(m+1 , N):  # makes lower traingle equal o zero
        mult = A[i , m]
        A[i,:] -= mult*A[m,:]
        v[i] -= v[m]*mult 


x = np.array([0.,0.,0.,0.],float)

for m in range(N-1, -1 , -1):   #Back Substitution
    x[m] = v[m]
    for i in range(m+1 ,N):  
        x[m] -= A[m,i]*x[i]


print "x=" , x
 

x_np = solve(A,v)
 
print "x from numpy=" , x_np 
