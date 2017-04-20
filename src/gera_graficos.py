import os
import numpy as np
import scipy as sp
from scipy import stats
import matplotlib.pyplot as plt
import sys
import math

input_size = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

#Grafico mandelbrot_seq

fig = plt.figure(1)

fig.suptitle('1 Thread')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo gasto')


seq_elephant = [0.000911988, 0.001947579, 0.005810300, 0.021446828, 0.084371574, 0.335577493, 1.335835770, 5.505320427, 21.618584923, 88.499974297]
seq_full = [0.004342094, 0.001383223, 0.003042832, 0.004556242, 0.016193319, 0.066050534, 0.262612604, 1.022417810, 4.340282105, 17.951102282]
seq_seahorse = [0.000922286, 0.001980260, 0.006083679, 0.022501505, 0.089204788, 0.353246800, 1.414779058, 5.853969199, 23.400544848, 93.346398082]
seq_triple_spiral = [0.001118846, 0.002167216, 0.006845384, 0.025581389, 0.100892618, 0.400364173, 1.598103541, 6.405259670, 26.707453872, 108.143847179]

plt.scatter(input_size, seq_elephant, marker='o', s=20)
plt.scatter(input_size, seq_full, marker='p', s=20)
plt.scatter(input_size, seq_seahorse, marker='o', s=20)
plt.scatter(input_size, seq_triple_spiral, marker='o', s=20)

plt.xlim( (2**3, 2**14) )
plt.xscale('symlog', basex = 2)
#plt.yticks(np.arange(min(seq_elephant), max(seq_elephant), 5))
plt.grid()
fig.add_subplot(111)
plt.plot(input_size,seq_elephant)
fig.add_subplot(111)
plt.plot(input_size,seq_full)
fig.add_subplot(111)
plt.plot(input_size,seq_seahorse)
fig.add_subplot(111)
plt.plot(input_size,seq_triple_spiral)
plt.show()

#Grafico teste2

fig_teste2 = plt.figure()
axteste = fig_teste2.add_subplot(111)

fig_teste2.suptitle("teste2")
seq_values_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for xy in zip(input_size, seq_values_2):                                       # <--
    ax.annotate('%s' % xy[1], xy = xy, textcoords='data') # <--
plt.scatter(input_size, seq_values_2, marker='o', s=20)
plt.xscale('symlog', basex = 2)
plt.yticks(np.arange(min(seq_values_2), max(seq_values_2), 0.5))
plt.grid()
plt.plot(input_size,seq_values_2)
plt.show()

