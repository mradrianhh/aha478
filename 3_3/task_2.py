import numpy as np
import matplotlib.pyplot as plt
from math import pi

delta_t = 0.01
times = np.arange(0, 10, 0.01)
white_noise_dist = np.random.normal(0, 2, len(times))

def signal(frequency, times):
    return np.sin(2*pi*frequency*times)

def noised_signal(frequency, times):
    return np.sin(2*pi*frequency*times) + white_noise_dist

def moving_avg_filter(M):
    total = 0
    for k in range(-M,M+1):
        total += noised_signal(2, times - k)
    return total/(2*M+1)

fig, axs = plt.subplots(4)
axs[0].plot(times, noised_signal(2, times))
axs[0].plot(times, signal(2, times))

M_list = [3, 11, 21]
for i in range(len(M_list)):
    axs[i+1].plot(times, moving_avg_filter(M_list[i]))

plt.show()