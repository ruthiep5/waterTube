import numpy as np 
import time

# *=everything

# Model
# h = 1.93*x + 9

# PARAMETERS
dt = 0.5
nsteps = 51

# linear model
m = 1.93
b = 9

# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    h = m * modelTime + b
    print(t, h)






