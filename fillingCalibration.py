import numpy as np
import time
from ezGraph import *
from rStats import *

#Model
# h = 2t - 3.22

def avg(lst):
    return sum(lst)/len(lst)


#Parameters
dt = 1
nsteps = 30


# Model:
# - Representation of the real world.
# -- Requires some data about the real world.
# - Analytical model: Equation or function that represents (best fits) the data. 
# -- Linear, polynomial, exponential, sinusoidal, logarithmic, hyperbolic, radical. 
# -- Plug in an input and the equation gives the output. 
# --- h(t) = 2t + 7
# ---- input: t
# ---- output: h
# -- Only works for well behaved systems (simple systems). Not a whole lot of interactions that will introduce errors. Non-chaotic.
# -- often use calculus to find the equations
# - PHYSICAL MODELS - 
# -- Small scale physical thing (you can touch it).
# -- Can be more complex
# -- Problems with scaling
# - NUMERICAL MODELS
# -- Usually computer models because there's a lot of calculations (algebraic).
# -- Usually break the system into smaller parts that interact with each other.
# -- The computer is used to keep track of all the interactions.
# -- We'll focus on things that change over time.  
# -- We'll focus on finite difference models. 


# linear model
# m = 5.03
# b = -17.2

r = 2.25 #radius (cm)
Q = 30 # Volume inflow rate: (dv/dt) (cubic cm / s)
h = 0        #initial hight (cm)
k = 0.0      #outflow rate constant

x_measured = [1,7,12,17,22,26]
y_measured = [0,10,20,30,40,50]
y_modeled = []

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

    dh = Q * dt / (np.pi * r **2)
    h = h + dh

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

print('time:', x_measured)   
print('h_measured:', y_measured)
print("h_modeled:", y_modeled)

print(f'xavg measured =  {avg(x_measured)}')
print(f'yavg measured =  {avg(y_measured)}')
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
print(f'residual = {r}')


def dsq(lst1):
    n = len(lst1)
    s = 0
    for i in range(n):
       # print(i,lst1[i], lst2[i])
        d = (lst1[i] - avg(lst1)) ** 2
        s += d
    return s

d = dsq(y_measured)
print(f'difference = {d}')

def rSquared(lst1, lst2):
    r2 = 1 - (res(lst1, lst2) / dsq(lst1) )
    return r2

r2 = rSquared(y_measured, y_modeled)
print(f'r squared = {r2}')


#draw graph
graph.keepOpen()