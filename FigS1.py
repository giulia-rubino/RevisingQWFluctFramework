import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pylab

# 100 linearly spaced numbers

w = np.arange(0,5,0.02)
wNeg = np.arange(-5,0,0.02)

def f(a, beta, w):
    return beta/(2*np.pi*a)*np.exp(-(beta*w/a)**2/(4*np.pi))

def g(a, beta, w):
    return 2*beta/(np.pi**2*a)/((beta*w/(np.pi*a))**2+1)**2

# the function, which is y = x^2 here
# y = np.log(1/delta-1)
beta = 1
#b = 2/beta
a = 0.851852
b = 0.22654
p_c = f(a, beta, w)
p_q = g(a, beta, w)
p_cNeg = f(b, beta, wNeg)
p_qNeg = f(b, beta, wNeg)

# setting the axes at the centre
fig = plt.figure()
#ax = fig.add_subplot(1, 1, 1)
#ax.spines['left'].set_position('center')
#ax.spines['bottom'].set_position('zero')
#ax.spines['right'].set_color('none')
#ax.spines['top'].set_color('none')
#ax.xaxis.set_ticks_position('bottom')
#ax.yaxis.set_ticks_position('left')

# plot the function
pylab.plot(wNeg,p_qNeg, color="#B4BDFF", solid_capstyle='round', linewidth=4)
pylab.fill_between(wNeg,p_qNeg, color="#B4BDFF", alpha=0.25)
pylab.plot(w,p_q, color="#B4BDFF", solid_capstyle='round', label=r'$p_q(w_d)$', linewidth=4)
pylab.fill_between(w,p_q, color="#B4BDFF", alpha=0.25)

pylab.plot(wNeg,p_cNeg, color="#F3B664", solid_capstyle='round', linewidth=4, linestyle='dotted')
pylab.fill_between(wNeg,p_cNeg, color="#F3B664", alpha=0.25)
pylab.plot(w,p_c, color="#F3B664", solid_capstyle='round', label=r'$p_c(w_d)$', linewidth=4)
pylab.fill_between(w,p_c, color="#F3B664", alpha=0.25)

plt.xlabel(r'$\beta w_d$', size=18)
plt.ylabel(r'$p(w_d)$', size=18)

matplotlib.rcParams['legend.fancybox'] = True
matplotlib.rcParams['legend.loc'] = 'best'
#matplotlib.rcParams['legend.numpoints'] = 2
matplotlib.rcParams['legend.fontsize'] = 'small'
matplotlib.rcParams['legend.framealpha'] = 0.3
#matplotlib.rcParams['legend.scatterpoints'] = 3
matplotlib.rcParams['legend.edgecolor'] = 'grey'
#
plt.legend(prop={"size":18})

# show the plot
plt.show()
fig.savefig("kind_distributions1.pdf")