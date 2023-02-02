### --- General Tips -- ###

# Importing matplotlib

import matplotlib.pyplot as plt
import numpy as np

plt.style.use('classic')

# show() or No show()? how to display your plots
## Plotting from a script

x = np.linspace(0, 10, 100)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))

plt.show()



