#!/usr/bin/env python
from tkinter import TclError
import matplotlib.pyplot as plt
import numpy as np
import time

intial_n = 10
step = 2
window = 20

# initial data
x = np.arange(intial_n)
y = np.random.rand(intial_n)

# create and show the figure in nonblocking mode
fig = plt.figure()
lines = plt.plot(x, y)
line = lines[0]
axes = line.axes
axes.set_ylim([0, 1])
plt.show(block=False)

# mark the time
last_draw = time.time()

def update_line_data():
    global x, y
    x = np.append(x, np.arange(x[-1] + 1, x[-1] + 1 + step))
    y = np.append(y, np.random.rand(step))

    if len(x) > window:
        x = x[len(x) - window:]
    if len(y) > window:
        y = y[len(y) - window:]
    line.set_data([x, y])
    line.axes.set_xlim([x[0] - 0.45, x[-1] + 0.45])
    line.axes.set_xticks(x)
    return x, y, line

while True:
    fig.canvas.draw_idle()
    try:
        fig.canvas.flush_events()
    except NotImplementedError:
        pass
    except TclError:
        # user closed the window
        break

    if (time.time() - last_draw) > 1:
        last_draw = time.time()
        update_line_data()

