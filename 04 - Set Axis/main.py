import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat Data
# sin(2wt + theta)
def sinusGenerator(amplitudo, frekuensi, takhir, theta):
    t = np.arange(0, takhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y

t1,y1 = sinusGenerator(1,1,4,0)

# 2. Membuat Plot
plt.plot(t1, y1)

# setting axis, minimum & maximum
plt.axis([0, 4, -2, 2])

# 3. Menampilkan Plot
plt.show()