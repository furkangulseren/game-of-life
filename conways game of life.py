import numpy as np
import matplotlib
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import random


N = 55
data = np.ones((N, N)) * 1
data.ravel()[np.random.choice(data.size, N, replace=False)] = np.nan # data.size = Number of elements in the array.
# random.choice() : Random sample from 1-D array


fig, ax = plt.subplots(1, 1, tight_layout=True)
my_cmap = matplotlib.colors.ListedColormap(['white']) # cmap: Colormap instance
my_cmap.set_bad(color='green', alpha=1) # alpha : blending value, between 0 (transparent) and 1 (opaque). 

fig = plt.gcf() # gcf: Get the current figure - left-corner title is changed.
fig.canvas.set_window_title('SEKOM YAZILIM')

ax.title.set_text('Conway\'s Game of Life')
ax.imshow(data, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)


def animate(x):
    global data
    data2=data.copy() # copy() makes it duplicate but without dependence to 'data'

    for i in range(N):
        for j in range(N):
            # print(data[i,j])
            if str(data[i, j]) == "nan" or data[i,j]==0:

                c = findNeighboursAlive(i, j)

                if c == 3:
                    data2[i, j] = 1 # become alive... from dead state to alive state
            else:
                q = findNeighboursAlive(i, j)
                # print(q)
                if q < 2 or q > 3:
                    data2[i, j] = np.nan # become dead... from alive state to dead state
    data=data2

    ax.imshow(data2, interpolation='none', cmap=my_cmap, extent=[0, N, 0, N], zorder=0)

    return [data2]


def findNeighboursAlive(i, j): # check 8 neighbors
    counter = 0
    try:
        if str(data[i - 1, j - 1]) != "nan":
            counter += 1
        if str(data[i - 1, j]) != "nan":
            counter += 1
        if str(data[i - 1, j + 1]) != "nan":
            counter += 1
        if str(data[i, j - 1]) != "nan":
            counter += 1
        if str(data[i, j + 1]) != "nan":
            counter += 1
        if str(data[i + 1, j + 1]) != "nan":
            counter += 1
        if str(data[i + 1, j]) != "nan":
            counter += 1
        if str(data[i + 1, j - 1]) != "nan":
            counter += 1
    except IndexError:
        pass
    return counter

anim = animation.FuncAnimation(fig, animate, interval=1, save_count=30) # interval decreases then speed of cellular increases -- save_count : number of values from *frames* to cache
plt.show()

