import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for k in range(N//2+1):  
        for n in range(N):    
            c[k] += y[n]*np.exp(-2j*np.pi*k*n/N)
    return c
 
N = 25
x = np.linspace(0. , 1. , N)
y = np.sin(np.pi*x/N)*np.sin(20*np.pi*x/N)
coeff = dft(y)
plt.plot(np.arange(len(coeff)), np.abs(coeff)**2) 
plt.savefig("sin coeff.jpeg", format="jpeg")
#plt.show()


t = np.linspace(0 , 1  , N)
y = t
coeff = dft(y)
plt.plot(np.arange(len(coeff)), np.abs(coeff)**2)
plt.savefig("sawtooth coeff.jpeg", format="jpeg")
#plt.show()

s = np.linspace(0 , 1 , N)
y = signal.square(2*np.pi*1*s)
coeff = dft(y)
plt.plot(np.arange(len(coeff)), np.abs(coeff)**2)
plt.savefig("square wave coeff.jpeg", format="jpeg")
plt.show()

