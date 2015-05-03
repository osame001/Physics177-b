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

plt.savefig("polynomial.png" , fromat="png")
 

### Zeros of the function ###

def f(x): 
    return 924 * (x**6) - 2772 * (x**5) + 3150 * (x**4) - 1680 * (x**3) + 420 * (x**2) - 42*x +1

x0 = np.array([0.0 , 0.2 , 0.4 , 0.6 , 0.8 , 1.0], float) # initial points 

sol = np.zeros(6, float)
for i in range(6):
    sol[i] = opt.newton(f, x0[i] , tol=1.e-10 , maxiter= 100) # using scipy function
print sol

