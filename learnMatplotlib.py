import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# Gen data
x = np.arange(0, 6, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# draw chart
plt.plot(x, y1, label="sin")
plt.plot(x, y2, linestyle="--", label="cos")
plt.xlabel("x")
plt.ylabel("y")
plt.title("sin&cos")
plt.legend()
plt.show()

# img = imread('/Users/travisliu/Documents/AMIS/Myself.png')
# plt.imshow(img)
#plt.show()

a = np.zeros([3, 2])
a[0, 0] = 1
a[0, 1] = 2
a[1, 0] = 9
a[2, 1] = 12
plt.imshow(a, interpolation="nearest")
plt.show()

