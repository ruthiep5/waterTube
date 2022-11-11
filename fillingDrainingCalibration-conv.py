import numpy as np
import time
from ezGraph import *
from rStats import *

#difference model
startTime = time.perf_counter()

#Parameters
dt = 10
nsteps = 200
conv = 0.01         #Convergence Criteria

r = 2.25 #radius (cm)
Q = 30 # Volume inflow rate: (dv/dt) (cubic cm / s)
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

    h_old = h

    # Filling
    dh = Q * dt / (np.pi * r **2)
    h = h + dh

    # Draining
    dVdt = -k * h 
    dh = dVdt * dt / (np.pi * r**2)
    h = h + dh
    
    # save height (h) calculated by the model
    #  only if the model time corresponds to one
    #  of the times when a measurement was taken
    
    graph.add(modelTime, h)
    #graph.wait(0.01)

    dh = h - h_old
    if dh < conv:
        break

endTime = time.perf_counter()

runtime = endTime-startTime
print(f'runtime: {runtime}')


print(modelTime, 'equilibrium =', h)

#draw graph
graph.keepOpen()