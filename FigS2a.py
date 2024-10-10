
#
# libraries
# libraries
import matplotlib.pyplot as plt
#plt.style.use('seaborn-whitegrid')
import numpy as np

eps = 15
eps1 = 3

def W(x, y, z):
    return -x/2-1/2*np.sqrt(x**2+(y/z)**2)

def alpha2(x, y, z):
    return (1-x/np.sqrt(x**2+(y/z)**2))/2

def beta2(x, y, z):
    return (1+x/np.sqrt(x**2+(y/z)**2))/2

def alphabeta(x, y, z):
    return (y/z/np.sqrt(x**2+(y/z)**2))/2

def overl0(x, y, z, th):
    return alpha2(x, y, z)*np.cos(th/2)**2 + beta2(x, y, z)*np.sin(th/2)**2 + alphabeta(x, y, z)*np.sin(th)

def overl1(x, y, z, th):
    return beta2(x, y, z)*np.cos(th/2)**2 + alpha2(x, y, z)*np.sin(th/2)**2 - alphabeta(x, y, z)*np.sin(th)

delta = 0.1
theta = np.pi/2

fig = plt.figure()


plt.vlines(x=0, ymin = 0, ymax=(1-delta)/2*np.cos(theta/2)**2, color='#322222', linewidth=14, label=r'$\mathcal{P}_{E_0,E_0}$', capstyle='round')
plt.vlines(x=eps1, ymin = 0, ymax=(1-delta)/2*np.cos(theta/2)**2, color='#704F4F', linewidth=14, label=r'$\mathcal{P}_{E_0,E_1}$', capstyle='round')
plt.vlines(x=-eps, ymin = 0, ymax=(1-delta)/2*np.sin(theta/2)**2, color='#A77979', linewidth=14, label=r'$\mathcal{P}_{E_1,E_0}$', capstyle='round')
plt.vlines(x=eps1-eps, ymin = 0, ymax=(1-delta)/2*np.sin(theta/2)**2, color='#C89B9B', linewidth=14, label=r'$\mathcal{P}_{E_1,E_1}$', capstyle='round')


plt.vlines(x=-W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl0(eps, eps1, delta, theta), color='#9EC8B9', linewidth=14, label=r'$\mathcal{P}_{E_0+\tilde{W}_0,E_0}$', capstyle='round')
plt.vlines(x=eps1-W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl0(eps, eps1, delta, theta), color='#5C8374', linewidth=14, label=r'$\mathcal{P}_{E_0+\tilde{W}_0,E_1}$', capstyle='round')
plt.vlines(x=-eps+W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl1(eps, eps1, delta, theta), color='#1B4242', linewidth=14, label=r'$\mathcal{P}_{E_1+\tilde{W}_1,E_0}$', capstyle='round')
plt.vlines(x=eps1-eps+W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl1(eps, eps1, delta, theta), color='#092635', linewidth=14, label=r'$\mathcal{P}_{E_1+\tilde{W}_1,E_1}$', capstyle='round')

print(+W(eps, eps1, delta))

plt.ylim(0, 0.4)
plt.xticks(fontsize=32)
plt.yticks(fontsize=32)
plt.legend(prop={"size":32}, loc="upper left")
plt.xlabel(r'$E_i-E_j$', size=32)
plt.show()
fig.savefig("2D_hist.pdf")