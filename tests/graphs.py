import matplotlib.pyplot as plt
from scipy.interpolate import interp1d
import numpy as np


xdata = [1,2,3,4,5,6,7,8,9,10]
ITERATION1=[152.942, 151.894, 151.894, 151.894, 151.422, 151.422, 151.422, 151.422, 151.175, 151.175]
ITERATION2=[151.117, 151.117, 151.117, 151.117, 151.117, 151.117, 150.864, 150.864, 150.864, 150.864]
ITERATION3=[152.053, 150.192, 150.192, 150.192, 150.192, 150.192, 150.192, 150.192, 150.192, 150.192]
ITERATION4=[151.431, 151.431, 150.733, 150.733, 150.733, 150.733, 150.733, 150.733, 150.733, 150.733]
ITERATION5=[151.592, 151.467, 151.467, 151.467, 151.467, 151.467, 151.467, 151.467, 151.467, 151.467]
ITERATION6=[152.542, 152.542, 152.228, 152.228, 152.228, 151.519, 151.519, 151.519, 150.531, 150.531]
ITERATION7=[151.392, 151.392, 151.267, 151.267, 151.156, 151.156, 151.156, 151.156, 151.156, 151.156]
ITERATION8=[152.203, 152.203, 152.203, 151.506, 151.506, 151.506, 151.506, 151.506, 150.678, 150.678]
MOYEN=[151.909, 151.53, 151.388, 151.3, 151.228, 151.139, 151.107, 151.107, 150.849, 150.849]
ECARTTYPE=[0.592, 0.612, 0.577, 0.714, 0.447, 0.437, 0.559, 0.559, 0.543, 0.543]



x = np.linspace(1, 10, 100)

plt.grid(True)

func = interp1d(xdata, ITERATION1, kind='cubic')
plt.plot(x, func(x), label='iteration1')

func = interp1d(xdata, ITERATION2, kind='cubic')
plt.plot(x, func(x), label='iteration2')

func = interp1d(xdata, ITERATION3, kind='cubic')
plt.plot(x, func(x), label='iteration3')

func = interp1d(xdata, ITERATION4, kind='cubic')
plt.plot(x, func(x), label='iteration4')

func = interp1d(xdata, ITERATION5, kind='cubic')
plt.plot(x, func(x), label='iteration5')

func = interp1d(xdata, ITERATION6, kind='cubic')
plt.plot(x, func(x), label='iteration6')

func = interp1d(xdata, ITERATION7, kind='cubic')
plt.plot(x, func(x), label='iteration7')

func = interp1d(xdata, ITERATION8, kind='cubic')
plt.plot(x, func(x), label='iteration8')

plt.xlabel('10^5')
plt.ylabel('Fitness')
plt.legend()
#plt.title()
plt.show()
#plt.savefig('0.png', transparent=True, dpi = 200)