import numpy as np
import matplotlib.pyplot as plt
from pylab import ylim, xlim , plot

data = np.loadtxt("sunspots.txt")
fig  = plt.figure()
ax = fig.add_subplot(111)

month = data[:,0]
spot = data[:,1]
#ax.plot(month , data, color="b" )
plt.savefig("sunspot.jpeg" , format = "jpeg")
ylim(0 , 10e8)
#xlim(0 , 3300)

y = np.zeros(len(spot))


def dft(y):
    N = len(y)
    c = np.zeros(N//2+1, complex)
    for w in range(N//2+1):
        for t in range(N):
            c[w] += y[t]*np.exp(-2j*np.pi*w*t/N)
    return c



y = spot

c1 = dft(y)

plot(abs(c1)**2)
plt.show()


