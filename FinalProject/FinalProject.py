import matplotlib
matplotlib.use("AGG")
import numpy as np
import h5py
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import scatter, show , xlabel , ylabel , plot
from matplotlib.pyplot import xlim, ylim
from scipy.optimize import curve_fit

f1 = h5py.File("snapshot_001.hdf5","r")
f5 = h5py.File("snapshot_005.hdf5","r")
#fig = plt.figure()

data5 = np.array(f5[u'PartType1'][u'Coordinates'])

### Going to CoM-Position- SnapShot #5 ###
posx = data5[:,0]
posy = data5[:,1]
posz = data5[:,2]

xc = np.sum(posx)/len(posx)
yc = np.sum(posy)/len(posy)
zc = np.sum(posz)/len(posz)

Xc = 0
Yc = 0
Zc = 0


deltax = Xc - xc
deltay = Yc - yc
deltaz = Zc - zc

r = np.sqrt(posx**2 + posy**2 + posz**2)

ix = r<500


while abs(deltax)>.1 or abs(deltay)>.1 or abs(deltaz)>.1:
    Xc = xc
    Yc = yc
    Zc = zc
    posx = posx -xc
    posy = posy -yc
    posz = posz -zc
    r = np.sqrt(posx**2 + posy**2 + posz**2)
    ix = r<500
    xc = np.sum(posx[ix])/float(len(posx[ix]))
    yc = np.sum(posy[ix])/float(len(posy[ix]))
    zc = np.sum(posz[ix])/float(len(posz[ix]))
    deltax = xc - Xc
    deltay = yc - Yc
    deltaz = zc - Zc


###--- 

### Claculating Density Profile ###
r_min = 20
r_max = 500
lr_min = np.log10(r_min)
lr_max = np.log10(r_max)
N_bin = 20
dlr = (lr_max - lr_min)/N_bin
n = np.zeros(N_bin)
rho = np.zeros(N_bin)
dis = np.zeros(N_bin)

for i in range(N_bin):
    r_bin = 10**(lr_min+(i+1)*dlr)
    aux = r < r_bin
    n[i] = len(r[aux])
    rho[i] = 1.1*n[i]/( 4* np.pi*(r_bin**3)/3)
    dis[i] = r_bin

### Curve-Fit ###

def NFW(dis , p1 , p2):
    return 3* p1 * (p2/dis)**3 * ( np.log((p2+dis)/p2) -dis/(p2 + dis) )

popt , pcov = curve_fit(NFW, dis , rho)


### Plotting Density and CurveFit ###
fig1 = plt.figure()
ax1 = fig1.add_subplot(111)

ax1.plot(dis ,rho, "o", label="GADGET")
ax1.plot(dis, NFW(dis , *popt), label="NFW Profile")

ax1.axhline(y= 5.55e-6, color="r", label="Critical Density")  ### The number "5$
ax1.set_xscale("log")
ax1.set_yscale("log")
ax1.set_title("Density Profile")
ax1.set_ylabel("Density in 1e10 solar mass/kpc^3")
ax1.set_xlabel( "Distance in kpc")
ax1.annotate(  "R_virial/R_s~4.3",xy=(2.e2, 1.e-4) ,xytext=(3.e2 , 1.e-3))
ax1.legend()
#fig1.savefig("FP-Curvefit.jpeg" , format="jpeg")



r_0 = 1000
### 3D Scatter-Plot for Particles ###
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection="3d")
ax2.scatter(posx, posy, posz, s=0.01)
ax2.set_xlim(-r_0, r_0)
ax2.set_ylim(-r_0, r_0)
ax2.set_zlim(-r_0, r_0)
fig2.savefig("FP 3D scatter r=1000 snapshot5.jpeg" , format="jpeg") 


### 2D Cross Section of Particle Positions ###

### CoM for particles in Snapshot#1 ###

data1 = np.array(f1[u'PartType1'][u'Coordinates'])

posx1 = data1[:,0]
posy1 = data1[:,1]
posz1 = data1[:,2]

xc1 = np.sum(posx1)/len(posx1)
yc1 = np.sum(posy1)/len(posy1)
zc1 = np.sum(posz1)/len(posz1)

Xc1 = 0
Yc1 = 0
Zc1 = 0


deltax1 = Xc1 - xc1
deltay1 = Yc1 - yc1
deltaz1 = Zc1 - zc1

r = np.sqrt(posx1**2 + posy1**2 + posz1**2)

ix = r<500


while abs(deltax1)>.1 or abs(deltay1)>.1 or abs(deltaz1)>.1:
    Xc1 = xc1
    Yc1 = yc1
    Zc1 = zc1
    posx1 = posx1 -xc1
    posy1 = posy1 -yc1
    posz1 = posz1 -zc1
    r = np.sqrt(posx1**2 + posy1**2 + posz1**2)
    ix = r<500
    xc1 = np.sum(posx1[ix])/float(len(posx1[ix]))
    yc1 = np.sum(posy1[ix])/float(len(posy1[ix]))
    zc1 = np.sum(posz1[ix])/float(len(posz1[ix]))
    deltax1 = xc1 - Xc1
    deltay1 = yc1 - Yc1
    deltaz1 = zc1 - Zc1


###--- 

### 3D Scatter-Plot for Particles ###

r_1 = 20000
fig3 = plt.figure()
ax3 = fig3.add_subplot(111, projection="3d")
ax3.scatter(posx1, posy1, posz1, s=0.01)
ax3.set_xlim(-r_1, r_1)
ax3.set_ylim(-r_1, r_1)
ax3.set_zlim(-r_1, r_1)
fig3.savefig("FP-3D scatter r=20000 snapshot1.jpeg" , format="jpeg")

### Velocity ###
datav1 = np.array(f1[u'PartType1'][ u'Velocities'])
datav5 = np.array(f5[u'PartType1'][ u'Velocities'])

velx1 = datav1[:,0]
vely1 = datav1[:,1]
velz1 = datav1[:,2]


velx5 = datav5[:,0]
vely5 = datav5[:,1]
velz5 = datav5[:,2]


### Pos-Vel for different coordinate for snapshot#5 ###
fig31 = plt.figure()
ax31 = fig31.add_subplot(311 )
ax31.scatter(posx ,  velx5, s=0.001  )
ax31.annotate( "Posx-Velx snapshot5",color="b",xy=(1.e4, 3.e3) ,xytext=(8.3e3 , 3.1e3))

ax32 = fig31.add_subplot(312)
ax32.scatter(posy, vely5, s=0.001)
ax32.annotate( "Posy-Vely snapshot5",color="r",xy=(1.e4, 3.e3) ,xytext=(1.e4 , 3.1e3))

ax33 = fig31.add_subplot(313)
ax33.scatter(posz , velz5 , s=0.001)
ax33.annotate( "Posz-Velz snapshot5",color="g",xy=(2.e4, 3.e3) ,xytext=(1.6e4 , 3.1e3))
#fig31.savefig("FP pos-vel.jpeg" , format="jpeg")

### Posx-Velx for snapshot #1 and #5 ###
fig41 = plt.figure()
ax41 = fig41.add_subplot(211)
ax41.scatter(posx ,  velx5, s=0.01)
ax41.annotate( "Posx-Velx snapshot5",color="b",xy=(1.e4, 3.e3) ,xytext=(8.3e3 , 3.1e3))

ax42 = fig41.add_subplot(212)
ax42.scatter(posx1 , velx1 , s=0.01)
ax42.annotate( "Posx-Velx snapshot1",color="b",xy=(1.e4, 2.e3) ,xytext=(8.3e3 , 2.1e3))
#fig41.savefig("FP posx-velx snapshots 1&5.jpeg", format="jpeg")




