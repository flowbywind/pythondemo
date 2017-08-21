import numpy as np
from scipy.ndimage import filters
import io
import matplotlib
import matplotlib.image as mpimg
img = np.zeros((300, 300))
img[np.random.randint(0, 300, 1000), np.random.randint(0, 300,
1000)] = 255
img2 = filters.gaussian_filter(img, 4, order=2)
import io
import matplotlib
import matplotlib.image as mpimg
from IPython import display
buf = io.BytesIO()
matplotlib.image.imsave(buf, img2, cmap="gray")
display.Image(buf.getvalue())