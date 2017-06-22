import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import data, color

# Load the example image and turn it into grayscale
image = cv2.imread('/Users/sathvik/work/python/RetinaDiag/imgs/src/RetinalScan/im0001.ppm')

# Compute the horizontal gradient using the centered 1D filter
# This is equivalent to replacing each non-border pixel with the
# difference between its right and left neighbors. The leftmost
# and rightmost edges have a gradient of 0.
gx = np.empty(image.shape, dtype=np.double)
gx[:, 0] = 0
gx[:, -1] = 0
gx[:, 1:-1] = image[:, :-2] - image[:, 2:]

# Same deal for the vertical gradient
gy = np.empty(image.shape, dtype=np.double)
gy[0, :] = 0
gy[-1, :] = 0
gy[1:-1, :] = image[:-2, :] - image[2:, :]

# Matplotlib incantations
fig, (ax1, ax2, ax3) = plt.subplots(3, 1,
                                    figsize=(5, 9),
                                    sharex=True,
                                    sharey=True)

ax1.axis('off')
ax1.imshow(image, cmap=plt.cm.gray)
ax1.set_title('Original image')
ax1.set_adjustable('box-forced')

ax2.axis('off')
ax2.imshow(gx, cmap=plt.cm.gray)
ax2.set_title('Horizontal gradients')
ax2.set_adjustable('box-forced')

ax3.axis('off')
ax3.imshow(gy, cmap=plt.cm.gray)
ax3.set_title('Vertical gradients')
ax3.set_adjustable('box-forced')
