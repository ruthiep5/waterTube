import numpy as np 
import time

# *=everything

# Model
# h = 1.93*x + 9

# PARAMETERS
dt = 1
nsteps = 30

# linear model
c = 53.5
b = -3.8
a = 0.9921

# TIME LOOP
for t in range(nsteps):
    modelTime = t * dt
    h = c * (a**modelTime) + b
    print(modelTime, h)






