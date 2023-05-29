#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2013,2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
ypoints = np.array([473615, 1027106, 1633774, 2561121, 2385645, 3720273,11001372, 8025363, 5601000,1607292, 353169 ])

plt.plot(xpoints, ypoints)
plt.show()

#Two  lines to make our compiler able to draw:
plt.savefig("cheaters.png")
sys.stdout.flush()