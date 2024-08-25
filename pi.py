import matplotlib.pyplot as plt
import numpy as np

xmax = 1_000_000
yrange = 1.5

def sin(x):
    try:
        return np.sin(160*x)
    except ZeroDivisionError:
        return 0
    
def csc(x):
    try:
        return 1.0 / np.sin(160*x)
    except ZeroDivisionError:
        return 0

def flr(x):
    try:
        return x - np.floor(x)
    except ZeroDivisionError:
        return 0

def mul60(x):
    return 160*x

def diri(x):
    return ...

xpoints = np.arange(1, xmax)
ypoints = np.apply_along_axis(flr, 0, xpoints)
# xpoints = np.apply_along_axis(mul60, 0, xpoints)

print(xpoints)
print(ypoints)
plt.ylim(-yrange, yrange) 
plt.xlim(1, xmax)
plt.scatter(xpoints, ypoints, s=1)

plt.show()