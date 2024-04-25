import matplotlib.pyplot as plt
import numpy as np

xmax = 250_000
yrange = 50_000

def f(x):
    try:
        return 1.0 / np.sin(x)
    except ZeroDivisionError:
        return 0

xpoints = np.arange(1, xmax)
ypoints = np.apply_along_axis(f, 0, xpoints)

print(xpoints)
print(ypoints)
plt.ylim(-yrange, yrange) 
plt.xlim(1, xmax)
plt.scatter(xpoints, ypoints, s=1)

plt.show()