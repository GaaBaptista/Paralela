import numpy as np
import matplotlib.pyplot as plt

fig= plt.subplots()
plt.title('Elephant Valley pthread')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo gasto')

input_size = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

pth_elephant_1 = [0.001005060, 0.001943597, 0.005734699, 0.020489631, 0.079562400, 0.315301019, 1.258185969, 5.026180836, 20.106780819, 81.181665197]
pth_elephant_2 = [0.001086002, 0.001757217, 0.003659727, 0.012258692, 0.045457151, 0.177593562, 0.707015861, 2.806535954, 11.341790358, 45.294231822]
pth_elephant_4 = [0.000983763, 0.001163847, 0.002338220, 0.006992166, 0.025594707, 0.100743140, 0.394875665, 1.646628861, 6.367647440, 26.711731595]
pth_elephant_8 = [0.001105832, 0.001132811, 0.001693929, 0.004247958, 0.014807217, 0.054712422, 0.251525071, 1.006903399, 3.996539720, 16.009348964]
pth_elephant_16 = [0.001041184, 0.001292822, 0.001539835, 0.003861766, 0.013611538, 0.052547608, 0.231009970, 0.910567991, 3.678390737, 14.648509657]
pth_elephant_32 = [0.001417263, 0.001620617, 0.002058744, 0.004235412, 0.012534250, 0.048014617, 0.227304661, 0.896609197, 3.576922553, 14.252888280]

bar_elephant_width = 1 / 7
index = np.arange(10)

bar_elephant_1 = plt.bar(index, pth_elephant_1, bar_elephant_width, label = '1 thread')
bar_elephant_2 = plt.bar(index + bar_elephant_width, pth_elephant_2, bar_elephant_width, label = '2 threads')
bar_elephant_4 = plt.bar(index + 2 * bar_elephant_width, pth_elephant_4, bar_elephant_width, label = '4 threads')
bar_elephant_8 = plt.bar(index + 3 * bar_elephant_width, pth_elephant_8, bar_elephant_width, label = '8 threads')
bar_elephant_16 = plt.bar(index + 4 * bar_elephant_width, pth_elephant_16, bar_elephant_width, label = '16 threads')
bar_elephant_32 = plt.bar(index + 5 * bar_elephant_width, pth_elephant_32, bar_elephant_width, label = '32 threads')

plt.xticks(index + 2.5 * bar_elephant_width, input_size)
plt.legend(fontsize = 'x-large')
plt.grid()
plt.show()