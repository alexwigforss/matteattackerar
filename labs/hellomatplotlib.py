import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import random

x = random.randint(100)

print(x)
print(matplotlib.__version__)

xypoints = np.array([[0, 2, 6],[36, 7, 23]])
xpoints = np.array([0, 2, 6, 4, 3, 6, 5, 8],ndmin=2)
ypoints = np.array([36, 7, 23])
# ypoints = np.array([0, 250])
print(xpoints)
# plt.plot(xpoints)
# plt.show()
hej = input()