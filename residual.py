import numpy as np

def resNumpy(lst1, lst2):
    d = np.array(lst1) - np.array(lst2)
    print(d)



x1 = [2, 5, 7]
x2 = [3, 1, 1]

def res(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = lst1[i] - lst2[i]
        s += d
        return s

r = res(x1, x2)
print(f'residual = {r}')

