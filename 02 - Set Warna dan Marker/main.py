import numpy as np
import matplotlib.pyplot as plt

# 1. Membuat Data
# sin(2wt + theta)
def sinusGenerator(amplitudo, frekuensi, takhir, theta):
    t = np.arange(0, takhir, 0.1)
    y = amplitudo * np.sin(2 * frekuensi * t + np.deg2rad(theta))
    return t,y


# 2. Membuat Plot
t1,y1 = sinusGenerator(1,1,4,0)
plt.plot(t1,y1)

t2,y2 = sinusGenerator(1,1,4,30)
plt.plot(t2, y2, 'r')

t3, y3 = sinusGenerator(1,1,4,60)
plt.plot(t3, y3, 'b--')

# 3. Tampilkan Plot
plt.show()

# Kumpulan Marker
# "."	point
# ","	pixel
# "o"	circle
# "v"	triangle_down
# "^"	triangle_up
# "<"	triangle_left
# ">"	triangle_right
# "1"	tri_down
# "2"	tri_up
# "3"	tri_left
# "4"	tri_right
# "8"	octagon
# "s"	square
# "p"	pentagon
# "P"	plus (filled)
# "*"	star
# "h"	hexagon1
# "H"	hexagon2
# "+"	plus
# "x"	x
# "X"	x (filled)
# "D"	diamond
# "d"	thin_diamond
# "|"	vline
# "_"	hline