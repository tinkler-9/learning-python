a, b = 1, [2,3]
print(id(a), id(b))

x = (a, b)
print(x)
b = [11,2,34]
b.append("c")
print(x)
y = (b, a)
print(id(x))
print(id(y))
print(id((b, a)), id((2, 1)))


import numpy as np
result = np.unique([1, 2, 1, 2, 1, 1, 3, 2, 1], return_counts=True)
print(result)
print(result[1])
print(type(result), len(result))
print(type(result[1]))

_, counts = np.unique([1, 2, 1, 2, 1, 1, 3, 2, 1], return_counts=True)
print(counts)