import numpy as np

n, m = map(int, input().strip().split())

arr = np.zeros((n, m))
for i in range(n):
    arr[i] = list(map(int, input().strip().split()))

mean_along_axis_1 = np.mean(arr, axis=1)
var_along_axis_0 = np.var(arr, axis=0)
std_along_axis_none = np.std(arr, axis=None)

print(mean_along_axis_1)
print(var_along_axis_0)
print(round(std_along_axis_none, 11))
