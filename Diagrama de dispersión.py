import matplotlib
import matplotlib.pyplot as plt
import statistics
import numpy as np

x_ran = np.random.randn(100)
y_ran = np.random.randn(100)
fig, ax = plt.subplots()
fig.suptitle('Diagrama de dispersion')
ax.scatter(x_ran, y_ran)
plt.show()
