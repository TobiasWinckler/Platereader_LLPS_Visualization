import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import matplotlib as mpl
from matplotlib.ticker import AutoMinorLocator

plt.rcParams["figure.figsize"] = [20, 12]
plt.rcParams["figure.autolayout"] = True


# data input and reshape to 8x12 array
data = np.array(pd.read_csv("data.CSV",sep = ';', header = None))
data_reshape = data.reshape(8, 12)


# normalize color map and apply to figure
norm = mpl.colors.BoundaryNorm(np.linspace(0, 2, 5), 10)
newcmap=cm.get_cmap('Purples', 10)
im = plt.imshow(data_reshape, interpolation='none', cmap=newcmap, norm=norm)
ax = plt.gca();


# ticks, tiltles and labels
ax.set_xticks([0,1,2,3,4,5,6,7,8,9,10,11]);
ax.set_yticks([0,1,2,3,4,5,6,7]);
ax.set_xticklabels([100,105,110,115,120,125,130,135,140,145,150,155],rotation=45,ha="right",
         rotation_mode="anchor");
ax.set_yticklabels([80, 70, 60, 50, 40, 30, 20, 5]);
ax.set_title("T=25°C    [KCl] = 200mM    t=2hrs")
ax.set_xlabel("[PEG] mg/mL")
ax.set_ylabel("[BSA] mg/mL")

# font size
plt.rcParams.update({'font.size': 40})



# contour line separating LLPS region
im = ax.contour(data_reshape, [0.5], colors='black', extend='none',linewidths=5)
im.clabel(fontsize=40, inline=1, fmt='%.2f')
plt.colorbar(label='$A_{600}$')
plt.text(8, 1, "LLPS region", color='white', fontdict={'size':40})



# grid lines and minor ticks
ax.xaxis.set_minor_locator(AutoMinorLocator(2))
ax.yaxis.set_minor_locator(AutoMinorLocator(2))
ax.tick_params(which='minor', length=0)
plt.grid(which='minor',linewidth=1.5)




# plot
plt.savefig('name.jpeg)
plt.show()
