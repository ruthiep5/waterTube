import numpy as np
import time
from ezGraph import *
from rStats import *

#Model

#Parameters
dt = 1
nsteps = 160

r = 2.25 #radius (cm)
Q = 0 # Volume inflow rate: (dv/dt) (cubic cm / s)
h = 50        #initial hight (cm)
k = 0.15    #outflow rate constant

x_measured = [0, 28, 60, 101, 157]
y_measured = [50, 40, 30, 20, 10]
y_modeled = [h]

#Graph
graph = ezGraphMM(xmax = 100,
    ymin=0, ymax=100,
    x_measured = x_measured,
    y_measured = y_measured,
    xLabel="Time (s)",
    yLabel="Height (cm)")


graph.addModeled(0,h)

#TIME LOOP
for t in range(nsteps):
  
    modelTime = t * dt

#filling
    dh = Q * dt / (np.pi * r **2)
    h = h + dh

#draining
    dVdt = -k * h 
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh

    if (modelTime in x_measured):
        print(modelTime, h)
        y_modeled.append(h)

    graph.addModeled(modelTime, h)
    #graph.wait(.1)

# s = 0
# def
# for i in x_measured:
#     s = s + x_measured
#     Ave = s / s.len
#     print(s)

# calculate average values

def absoluteError(lst1, lst2):
    n = len(lst1)
    a = 0
    for i in range(n):
        # print(i,lst1[i], lst2[i])
        d = lst1[i] - lst2[i]
        a += abs(d)
    return(a)

#residual
def res(lst1, lst2):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = (lst1[i] - lst2[i]) ** 2
        s += d
    return s

r = res(y_measured, y_modeled)


def avg(lst):
    return sum(lst)/len(lst)

def dsq(lst1):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = (lst1[i] - avg(lst1)) ** 2
        s += d
    return s

d = dsq(y_measured)

def rSquared(lst1, lst2):
    r2 = 1 - (res(lst1, lst2) / dsq(lst1) )
    return r2

r2 = rSquared(y_measured, y_modeled)


print('time:', x_measured)   
print('h_measured:', y_measured)
print("h_modeled:", y_modeled)
print(f'xavg measured =  {avg(x_measured)}')
print(f'yavg measured =  {avg(y_measured)}')
print(f'residual = {r}')
print(f'difference = {d}')
print(f'r squared = {r2}')

#draw graph
graph.keepOpen()
