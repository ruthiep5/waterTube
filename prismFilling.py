import numpy as np 
import time
import ezGraph

# *=everything

# Model
# h = 1.93*x + 9

# PARAMETERS
dt = 1
nsteps = 30

# linear model
w = 10
l = 5
h = 0

# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    
    dh = Q * dt / (np.pi * (r**2))
    h = h + dh

    print(modelTime, h)






