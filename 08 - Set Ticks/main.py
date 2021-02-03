import numpy as np
import matplotlib.pyplot as plt 

# membuat data
sudut = np.arange(0, 361)
y = np.sin(np.deg2rad(sudut))

# membuat plot
plt.plot(sudut, y)
plt.yticks([-1, 0, 1])
plt.xticks(
    [           0,            90,            180,            270,             360],
    [r'$ {0}^o $', r'$ {90}^o $', r'$ {180}^o $', r'$ {270}^o $', r'$ {360}^o $',]
    )

# menampilkan plot
plt.show()