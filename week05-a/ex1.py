### Plotting the function ###
import matplotlib.pylab as plt
from numpy import linspace
import pdb
from pylab import plot , show , ylim, xlabel , ylabel
import scipy.optimize as opt 
import numpy as np

x = linspace(0,1,100)
y = 924 * (x**6) - 2772 * (x**5) + 3150 * (x**4) - 1680 * (x**3) + 420 * (x**2) - 42*x +1

plot(x,y)
ylim(-1.1 , 1.1)
xlabel("x")
ylabel("Polynomial function")

#plt.savefig("polynomial.png" , fromat="png")
#show()
 

### Zeros of the function ###

#accuracy = 1e-10
#y(x) = (924 * (x**6) - 2772 * (x**5) + 3150 * (x**4) - 1680 * (x**3) + 420 * (x**2) - 42*x +1) 
#def y(x):
#    s = 0.0 
#    delta = 1.0
#    while abs(delta)>accuracy:
#        delta = ((924 * (s**6) - 2772 * (s**5) + 3150 * (s**4) - 1680 * (s**3) + 420 * (s**2) - 42*s +1))/ (6*924 * (s**5) - 5*2772 * (s**4) + 4*3150 * (s**3) - 3*1680 * (s**2) + 2*420 * (s**1) - 42)
#        x -= delta
#    return x
#    print x

def f(x): 
    return 924 * (x**6) - 2772 * (x**5) + 3150 * (x**4) - 1680 * (x**3) + 420 * (x**2) - 42*x +1

x0 = np.array([0.0 , 0.2 , 0.4 , 0.6 , 0.8 , 1.0], float) 
#sol1 = opt.newton(f, x0 , tol=1.e-10 , maxiter= 100) 
#print sol1
sol = np.zeros(6, float)
for i in range(6):
    sol[i] = opt.newton(f, x0[i] , tol=1.e-10 , maxiter= 100)
print sol

