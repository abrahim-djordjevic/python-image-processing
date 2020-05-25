import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def greyScale(img):
    #usesthe ITU-R 601-2 lima transform function to convert to grayscale
    return np.dot(img[...,:3], [0.2989, 0.5870, 0.1140])

filename = sys.argv[1]
img = mpimg.imread(filename)
greyimg = greyScale(img)
imgplot = plt.imshow(greyimg, cmap = plt.get_cmap('gray'),vmin=0,vmax=1)
plt.show()

