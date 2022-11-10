import numpy as np 
import time

# *=everything

# Model
# h = 2t - 3.22

# PARAMETERS
dt = 0.5
nsteps = 51

# linear model
m = 2
b = -3.22

# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    h = m * modelTime + b
    print(t, h)






