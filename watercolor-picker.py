import colorsys
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter

pi = np.asarray(Image.open('./palette.jpeg'))

values = np.sum(pi, axis=2)

values_h = np.max(values, axis=0)
values_v = np.max(values, axis=1)

print(values_h.shape)
print(values_v.shape)

plt.plot(list(range(values_v.shape[0])), values_v)
plt.show()

#hsv_pi = colorsys.rgb_to_hsv()
