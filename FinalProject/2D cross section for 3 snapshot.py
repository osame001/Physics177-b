import numpy as np
import h5py
import matplotlib.pyplot as plt


f1 = h5py.File("snapshot_001.hdf5","r")
f2 = h5py.File("snapshot_003.hdf5","r")
f3 = h5py.File("snapshot_005.hdf5","r")

fig = plt.figure()
plt.subplots_adjust(hspace=0.06)
plt.subplots_adjust(wspace=0.06)

data11 = np.array(f1[u'PartType1'][u'Coordinates'])

data21 = np.array(f2[u'PartType1'][u'Coordinates'])

data31 = np.array(f3[u'PartType1'][u'Coordinates'])

pos11x = data11[:,0]
pos11y = data11[:,1]
pos11z = data11[:,2]

xc11 = np.sum(pos11x)/len(pos11x)
yc11 = np.sum(pos11y)/len(pos11y)
zc11 = np.sum(pos11z)/len(pos11z)

ix11 = np.abs(pos11z-zc11)<500
ax11 = fig.add_subplot(331)
ax11.scatter(pos11x[ix11], pos11y[ix11], s=0.01, color="r")
plt.setp(plt.gca(),xticklabels=[])
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))


ix12 = np.abs(pos11x-xc11)<500
ax12 = fig.add_subplot(332)
ax12.scatter(pos11y[ix12], pos11z[ix12], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])
plt.setp(plt.gca(),xticklabels=[])


ix13 = np.abs(pos11y-yc11)<500
ax13 = fig.add_subplot(333)
ax13.scatter(pos11x[ix13], pos11z[ix13], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])
plt.setp(plt.gca(),xticklabels=[])


pos21x = data21[:,0]
pos21y = data21[:,1]
pos21z = data21[:,2]

xc21 = np.sum(pos21x)/len(pos21x)
yc21 = np.sum(pos21y)/len(pos21y)
zc21 = np.sum(pos21z)/len(pos21z)

ix21 = np.abs(pos21z-zc21)<500
ax21 = fig.add_subplot(334)
ax21.scatter(pos21x[ix21], pos21y[ix21], s=0.01, color="r")
plt.setp(plt.gca(),xticklabels=[])
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))


ix22 = np.abs(pos21x-xc21)<500
ax22 = fig.add_subplot(335)
ax22.scatter(pos21y[ix22], pos21z[ix22], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])
plt.setp(plt.gca(),xticklabels=[])


ix23 = np.abs(pos21y-yc21)<500
ax23 = fig.add_subplot(336)
ax23.scatter(pos21x[ix23], pos21z[ix23], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])
plt.setp(plt.gca(),xticklabels=[])


pos31x = data31[:,0]
pos31y = data31[:,1]
pos31z = data31[:,2]

xc31 = np.sum(pos31x)/len(pos31x)
yc31 = np.sum(pos31y)/len(pos31y)
zc31 = np.sum(pos31z)/len(pos31z)

ix31 = np.abs(pos31z-zc31)<500
ax31 = fig.add_subplot(337)
ax31.scatter(pos31x[ix31], pos31y[ix31], s=0.01, color="r")
plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))
plt.ticklabel_format(style='sci',axis='y',scilimits=(0,0))


ix32 = np.abs(pos31x-xc31)<500
ax32 = fig.add_subplot(338)
ax32.scatter(pos31y[ix32], pos31z[ix32], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])
plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))


ix33 = np.abs(pos31y-yc31)<500
ax33 = fig.add_subplot(339)
ax33.scatter(pos31x[ix33], pos31z[ix33], s=0.01, color="r")
plt.setp(plt.gca(),yticklabels=[])

plt.ticklabel_format(style='sci',axis='x',scilimits=(0,0))




plt.savefig("2-D cross sections 3 Particle type-2.jpeg", format="jpeg")
plt.show()


