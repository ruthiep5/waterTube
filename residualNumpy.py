import numpy as np

def resNumpy(lst1, lst2):
    d = np.array(lst1) - np.array(lst2)
    print(d)
    s = sum(d)
    return s

x1 = [2, 5, 7]
x2 = [3, 1, 1]

res = resNumpy(x1, x2)
print(f'residual = {res}')