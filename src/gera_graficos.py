import os
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import sys
import math

fig = plt.figure()
ax = fig.add_subplot(111)

fig.suptitle('1 Thread')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo gasto')

X = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
Y = [0.001013716, 0.000875231, 0.001174499, 0.003097618, 0.010853464, 0.041283986, 0.160114177, 0.637433311, 2.524890527, 9.625289915]
lbl = ['16', '32', '64', '128', '256', '512', '1024', '2048', '4096', '8192']
for xy in zip(X, Y):                                       # <--
    ax.annotate('%s' % xy[1], xy = xy, textcoords='data') # <--
plt.scatter(X, Y, marker='o', s=20)
plt.xscale('symlog', basex = 2)
plt.yticks(np.arange(min(Y), max(Y), 0.5))
plt.grid()
plt.plot(X,Y)
plt.show()


