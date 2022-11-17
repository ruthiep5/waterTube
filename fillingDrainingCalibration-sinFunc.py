import numpy as np
import time
import math
from ezGraph import *
from rStats import *

#difference model

#Parameters
dt = 1
nsteps = 100

r = 2.25 #radius (cm)
Qin = 30 # Volume inflow rate: (dv/dt) (cubic cm / s)
h = 0        #initial hight (cm)
k = 0.15      #outflow rate constant


#Experimental Data
y_modeled = []

#Graph
graph = ezGraph(xmin=0, xmax = 100,
                xLabel="Time (s)",
                yLabel="Height (cm)")
graph.add(0,h)


#Time Loop
for t in range(nsteps):
    modelTime = t * dt

    Qin = 10*math.sin(50*modelTime) + 11

    if Qin <= 0:
        Qin = 0

    # Filling
    dh = Qin * dt / (np.pi * r **2)
    h = h + dh

    # Draining
    dVdt = -k * h 
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh
    
    # save height (h) calculated by the model
    #  only if the model time corresponds to one
    #  of the times when a measurement was taken
    
    graph.add(modelTime, h)
    if t > 2:
        if (graph.y[-2] > graph.y[-1]) and (graph.y[-2] > graph.y[-3]):
            print(f"Max: {graph.y[-2]}")

        elif (graph.y[-2] < graph.y[-1]) and (graph.y[-2] < graph.y[-3]):
            print(f'Min {graph.y[-2]}')


#draw graph
graph.keepOpen()