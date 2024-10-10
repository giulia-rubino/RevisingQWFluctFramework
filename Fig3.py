import numpy as np
from qutip import *
import matplotlib.pyplot as plt

epsilon = 12
epsilon1 = 3

def f(x, y, z):
    return np.sqrt((1-x/np.sqrt(x**2+(y/z)**2))/2)

def g(x, y, z):
    return np.sqrt((1+x/np.sqrt(x**2+(y/z)**2))/2)

delta1 = 0.01
a1 = f(epsilon, epsilon1, delta1)
b1 = g(epsilon, epsilon1, delta1)
phi1 = np.arctan(b1/a1)

delta2 = 0.1
a2 = f(epsilon, epsilon1, delta2)
b2 = g(epsilon, epsilon1, delta2)
phi2 = np.arctan(b2/a2)

delta3 = 0.2
a3 = f(epsilon, epsilon1, delta3)
b3 = g(epsilon, epsilon1, delta3)
phi3 = np.arctan(b3/a3)

delta4 = 0.3
a4 = f(epsilon, epsilon1, delta4)
b4 = g(epsilon, epsilon1, delta4)
phi4 = np.arctan(b4/a4)

b = qutip.Bloch()
b.make_sphere()
b.vector_color = ['#F55050', '#F48484', '#E8D2A6', '#86A3B8']
b.xlabel = [r'$\vert E_+\rangle$', r'$\vert E_-\rangle$']
b.xlpos = [1.15,-1.18]
b.zlpos = [1.1,-1.1]
b.ylabel = ['', '']
b.zlabel = [r'$\vert E_0\rangle$', r'$\vert E_1\rangle$']

vec1 = [np.sin(2*phi1), 0, np.cos(2*phi1)]
b.add_vectors(vec1)
#b.add_annotation(vec1, r'$\delta = 0.01$',font=dict(size=16))
print('a1 = ', a1)
print('b1 = ', b1)
print('phi1 = ', phi1)

vec2 = [np.sin(2*phi2), 0, np.cos(2*phi2)]
b.add_vectors(vec2)
#b.add_annotation(vec2, r'$\delta = 0.1$',font=dict(size=16))
print('a2 = ', a2)
print('b2 = ', b2)
print('phi2 = ', phi2)

vec3 = [np.sin(2*phi3), 0, np.cos(2*phi3)]
b.add_vectors(vec3)
#b.add_annotation(vec3, r'$\delta = 0.2$',font=dict(size=16))
print('a3 = ', a3)
print('b3 = ', b3)
print('phi3 = ', phi3)

vec4 = [np.sin(2*phi4), 0, np.cos(2*phi4)]
b.add_vectors(vec4)
#b.add_annotation(vec4, r'$\delta = 0.3$',font=dict(size=16))
print('a4 = ', a4)
print('b4 = ', b4)
print('phi4 = ', phi4)

b.render()

plt.show()