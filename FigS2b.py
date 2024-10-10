
#
# libraries
# libraries
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
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


delta = np.arange(0.02,0.2,0.02)
theta = np.pi/2

y = W(eps, eps1, delta)
p1 = (1-delta)/2*np.cos(theta/2)**2
p2 = (1-delta)/2*np.sin(theta/2)**2
p3 = delta/2*overl0(eps, eps1, delta, theta)
p4 = delta/2*overl1(eps, eps1, delta, theta)

fig = plt.figure()
ax = plt.axes(projection='3d')

for i in range(7):
    ax.plot([delta[i],delta[i]],[0,0],[0,p1[i]], color='#322222', linewidth=7, label=r'$\mathcal{P}_{E_0,E_0}$')
    ax.plot([delta[i],delta[i]],[eps1,eps1],[0,p1[i]], color='#704F4F', linewidth=7, label=r'$\mathcal{P}_{E_0,E_1}$')
    ax.plot([delta[i],delta[i]],[-eps,-eps],[0,p2[i]], color='#A77979', linewidth=7, label=r'$\mathcal{P}_{E_1,E_0}$')
    ax.plot([delta[i],delta[i]],[eps1-eps,eps1-eps],[0,p2[i]], color='#C89B9B', linewidth=7, label=r'$\mathcal{P}_{E_1,E_1}$')
    ax.plot([delta[i],delta[i]],[-y[i],-y[i]],[0,p3[i]], color='#9EC8B9', linewidth=7, label=r'$\mathcal{P}_{E_0+W_0,E_0}$')
    ax.plot([delta[i],delta[i]],[eps1-y[i],eps1-y[i]],[0,p3[i]], color='#5C8374', linewidth=7, label=r'$\mathcal{P}_{E_0+W_0,E_1}$')
    ax.plot([delta[i],delta[i]],[-eps+y[i],-eps+y[i]],[0,p4[i]], color='#1B4242', linewidth=7, label=r'$\mathcal{P}_{E_1+W_1,E_0}$')
    ax.plot([delta[i],delta[i]],[eps1-eps+y[i],eps1-eps+y[i]],[0,p4[i]], color='#092635', linewidth=7, label=r'$\mathcal{P}_{E_1+W_1,E_1}$')


    #ax.plot([delta[i],delta[i]],[-eps1-y[i],-eps1-y[i]],[0,p5[i]], color='#63707E', linewidth=7, label=r'$\mathcal{P}_{E_0,E_1+W_2}$')
    #ax.plot([delta[i],delta[i]],[eps+y[i],eps+y[i]],[0,p6[i]], color='#93B5B3', linewidth=7, label=r'$\mathcal{P}_{E_1+W_1,E_0}$');


#plt.vlines(x=0, ymin = 0, ymax=(1-delta)/2*np.cos(theta/2)**2, color='#322222', linewidth=14, label=r'$\mathcal{P}_{E_0,E_0}$', capstyle='round')
#plt.vlines(x=eps1, ymin = 0, ymax=(1-delta)/2*np.cos(theta/2)**2, color='#704F4F', linewidth=14, label=r'$\mathcal{P}_{E_0,E_1}$', capstyle='round')
#plt.vlines(x=-eps, ymin = 0, ymax=(1-delta)/2*np.sin(theta/2)**2, color='#A77979', linewidth=14, label=r'$\mathcal{P}_{E_1,E_0}$', capstyle='round')
#plt.vlines(x=eps1-eps, ymin = 0, ymax=(1-delta)/2*np.sin(theta/2)**2, color='#C89B9B', linewidth=14, label=r'$\mathcal{P}_{E_1,E_1}$', capstyle='round')
#
#plt.vlines(x=W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl0(eps, eps1, delta, theta), color='#9EC8B9', linewidth=14, label=r'$\mathcal{P}_{E_0+W_0,E_0}$', capstyle='round')
#plt.vlines(x=eps1+W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl0(eps, eps1, delta, theta), color='#5C8374', linewidth=14, label=r'$\mathcal{P}_{E_0+W_0,E_1}$', capstyle='round')
#plt.vlines(x=-eps-W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl1(eps, eps1, delta, theta), color='#1B4242', linewidth=14, label=r'$\mathcal{P}_{E_1+W_1,E_0}$', capstyle='round')
#plt.vlines(x=eps1-eps-W(eps, eps1, delta), ymin = 0, ymax=delta/2*overl1(eps, eps1, delta, theta), color='#092635', linewidth=14, label=r'$\mathcal{P}_{E_1+W_1,E_1}$', capstyle='round')


#plt.zlim((0, 1))
#plt.legend(prop={"size":12}, loc="upper right")
plt.xlabel(r'$\epsilon$', size=16)
plt.ylabel(r'$E_i-E_j$', size=16)
plt.show()
fig.savefig("3D_Hist1.pdf")