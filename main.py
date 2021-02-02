import numpy as np 
import matplotlib.pyplot as plt 

# Buat Lingkaran
PI = np.pi 
sudut = np.linspace(0, 2*PI, 100)
r = 5
x = r*np.cos(sudut)
y = r*np.sin(sudut)

# Inisialisasi
plt.plot(x,y)

# Tampilkan
plt.show()