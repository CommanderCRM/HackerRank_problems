import numpy as np

a = np.array(input().split(), float)
x = float(input())

print(np.polyval(a, x))
