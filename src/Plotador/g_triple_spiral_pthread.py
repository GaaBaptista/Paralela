import numpy as np
import matplotlib.pyplot as plt

fig= plt.subplots()
plt.title('Triple Spiral Valley pthread')
plt.xlabel('Tamanho da entrada')
plt.ylabel('Tempo gasto')

input_size = [16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]

pth_triple_spiral_1 = [0.001023408, 0.002175376, 0.006705679, 0.024639747, 0.095864365, 0.380490393, 1.519804456, 6.074284673, 24.294932248, 98.000608917]
pth_triple_spiral_2 = [0.001184869, 0.001911902, 0.004422378, 0.015126102, 0.057950283, 0.230599144, 0.937818310, 3.581502472, 14.355670856, 57.804844264]
pth_triple_spiral_4 = [0.000962242, 0.001223073, 0.002455519, 0.007807843, 0.029144270, 0.115294132, 0.468129509, 1.897938625, 7.899992268, 30.526966265]
pth_triple_spiral_8 = [0.001207627, 0.001188089, 0.001827614, 0.004895684, 0.016718974, 0.073423290, 0.287714800, 1.146090715, 4.589728206, 18.195635493]
pth_triple_spiral_16 = [0.001060821, 0.001286565, 0.001743480, 0.004487179, 0.015828581, 0.066943383, 0.273606375, 1.090377972, 4.365142488, 17.255059378]
pth_triple_spiral_32 = [0.001478282, 0.001595763, 0.002094780, 0.004584579, 0.014506852, 0.069449128, 0.270402826, 1.072163211, 4.274765938, 17.110603862]

bar_triple_spiral_width = 1 / 7
index = np.arange(10)

bar_triple_spiral_1 = plt.bar(index, pth_triple_spiral_1, bar_triple_spiral_width, label = '1 thread')
bar_triple_spiral_2 = plt.bar(index + bar_triple_spiral_width, pth_triple_spiral_2, bar_triple_spiral_width, label = '2 threads')
bar_triple_spiral_4 = plt.bar(index + 2 * bar_triple_spiral_width, pth_triple_spiral_4, bar_triple_spiral_width, label = '4 threads')
bar_triple_spiral_8 = plt.bar(index + 3 * bar_triple_spiral_width, pth_triple_spiral_8, bar_triple_spiral_width, label = '8 threads')
bar_triple_spiral_16 = plt.bar(index + 4 * bar_triple_spiral_width, pth_triple_spiral_16, bar_triple_spiral_width, label = '16 threads')
bar_triple_spiral_32 = plt.bar(index + 5 * bar_triple_spiral_width, pth_triple_spiral_32, bar_triple_spiral_width, label = '32 threads')

plt.xticks(index + 2.5 * bar_triple_spiral_width, input_size)
plt.legend(fontsize = 'x-large')
plt.grid()
plt.show()