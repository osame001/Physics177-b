
### Electric Potential and Electric Field ###
### I assume that two particles are at: positive charge at (x0p , -1) and negative charge at (x0n , -1) ###
### 1m*1m was so big and I couldn't see and noticeable effect. So I considered a 1cm*1cm plate. ###

import numpy as np
import math 
from   pylab import imshow , show, quiver

x0n = 10
x0p= 0

e = 8.854187817

phi = np.zeros(shape=( 101 ,  101))
x = np.zeros(101)
y = np.zeros(101)

dx = 10**-4  # in meter unit
 
for i in range ( 101):
    for j in range ( 101):
        x[j] = j * dx
        y[i] = i * dx
        phi[i , j] = 100/(4 * e * math.pi) * ( ( (x[j]-x0p*dx)**2 + ( y[i]+ 10**-2 )**2  )**-0.5 - ( (x[j] - x0n*dx )**2 + (y[i] + 10**-2 )**2  )**-0.5 )
        
imshow(phi , origin = "lower")
show()

E_x = np.zeros(shape=(101, 101))
E_y = np.zeros(shape=(101, 101))
E = np.zeros(shape=(101, 101))
### electric field ###
for i in range (100):
    for j in range (100):
        E_x[i , j] = (phi[i+1,j]-phi[i,j])/dx
        E_y[i ,j] = ( phi[i , j+1]- phi[i , j])/dx
        

quiver(x,y,E_x,E_y)
show()
 
