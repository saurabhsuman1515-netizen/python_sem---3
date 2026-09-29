import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)

plt.show()




import numpy as np
from matplotlib import pyplot as plt
x = np.arange(1,11)

y = 2*x+5
plt.title("Line Plot")
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.plot(x,y)

plt.show()
