import numpy as np
import matplotlib.pyplot as plt

# Quadratic equation: y = x² - 4x + 3
x = np.linspace(-5, 5, 100)
y = x**2 - 4*x + 3

# Plot
plt.plot(x, y)

plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Equation: y = x² - 4x + 3")
plt.grid(True)

plt.show()