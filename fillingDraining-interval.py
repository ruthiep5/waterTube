import numpy as np
import time
from ezGraph import *
from rStats import *

#difference model

#Parameters
dt = 1.
nsteps = 200

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

    # if 0 == modelTime%5:
    #     if Qflag:
    #         Qflag = False
    #     else:
    #         Qflag = True
    # if Qflag:
    #     Qin = 30
    # else:
    #     Qin = 0
    # print(modelTime, Qflag, Qin)
    

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
    graph.wait(0.01)

#draw graph
graph.keepOpen()