import numpy as np
import matplotlib.pyplot as plt 

# membuat data
def sinusGenerator(amplitudo, frekuensi, takhir, theta):
    t = np.arange(0, takhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y


t1,y1 = sinusGenerator(1,1,4,0)

# membuat plot
plt.plot(t1,y1)
plt.text(1.7,0.5, r'$ \mathcal{Y} = A.sin(2 \omega t + \theta) $')
plt.text(1.7,0.4, r'$ \mathcal{A} = 1 cm, \omega = 1 Hz, \theta = 0{^o} $')


# menampilkan plot
plt.show()