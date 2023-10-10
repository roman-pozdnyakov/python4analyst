# Пример для рисования графиков в терминале
import numpy as np
from bashplotlib.histogram import plot_hist

arr = np.random.normal(size=1000, loc=0, scale=1)
plot_hist(arr, bincount=50)