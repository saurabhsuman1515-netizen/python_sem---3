import numpy as np

a = np.array([1, 2, 3, 4])
print("a\n",a)
print(a.shape)  ## give size

b = np.array([[1,2,4],[3,5,6]])
print("b:\n",b)
print(b.shape)  ##give row and coloumn
print(a.reshape((2,2)))


print(np.arange(2,20,2))
print(np.arange(9).reshape((3,3)))

a = np.arange(3, 20, 6)
print(a)

print(np.zeros((5,)))

print(np.ones((5,2)))



OneCol = np.ones((5,))
ZeroCols = np.zeros((5, 2))

print(np.column_stack((OneCol, ZeroCols)))

c = np.arange(12)
print(a[::2])