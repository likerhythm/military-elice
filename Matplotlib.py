import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline
# Jupyter 이용
x = np.random.rand(3)
y = np.random.rand(3)
z = np.random.rand(3)
data = [x, y, z]
fig, ax = plt.subplots()
x_ax = np.arange(3)
for i in x_ax:
    ax.bar(x_ax, data[i],
          bottom = np.sum(data[:i], axis = 0))
ax.set_xticks(x_ax)
ax.set_xticklabels(["A", "B", "C"])

plt.show()