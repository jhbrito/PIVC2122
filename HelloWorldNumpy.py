import numpy as np

a = np.array([1.2, 2, 3])
print("a", a)
print("type", type(a))
print("a[0]", a[0])


# arrays with types
a = np.ndarray( (10, 10), dtype=np.uint8)
print("a", a)
print("type", type(a))
print("a[0]:", a[0, 0])