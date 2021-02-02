import numpy as np 
import matplotlib.pyplot as plt 

# PENDAHULUAN PYPLOT

"""
Ada 3 step:
1. Membuat Data
2. Membuat Plot
3. Menampilkan Plot
"""

# 1. Membuat Data
x = np.array([1,2,3,4,5])
y = x**2
y2 = y**2

# 2. Membuat Plot
plt.plot(x,y)
plt.plot(x,y2)

# 3. Menampilkan Plot
plt.show()