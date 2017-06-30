import numpy as np
from time import time

array = np.zeros((10))
matrix = np.arange(0,10,.1)

print(array)

array[0] = 1

print(array)

str_arr = np.array(['hello world', 'other string'])

print(str_arr)

print(np.array(['string name', 123513]))

t = time()

np.arange(1, 10000000, .1)

print( time() - t)

t1 = time() - t

t = time()
list = []

for i in range(100000000):
    list.append(i)
t2 = time() - t
print(t2)

print(t2/t1)

