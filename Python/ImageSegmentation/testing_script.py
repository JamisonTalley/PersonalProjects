#testing_script.py
#Jamison Talley
#12-12-23

#import necessary libraries and segmentationClass
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
from segmentationClass import segmentationClass

# load test image from active directory using Pillow
im_1 = Image.open("testing_image.png")
# convert the image into an nxnx3 numpy array, and calculate value of n
image = np.array(im_1)
n = len(image)

# initialize instance of segmentationClass, and assign hyperparameter values
seg = segmentationClass()
seg.p0 = 1
seg.x_a = [2,3]
seg.x_b = [0,0]

# run the input image array through the segmentImage method
segmented_image_matrix = seg.segmentImage(image)

# make the numpy formatting easier to read
np.set_printoptions(linewidth = 5 * n + 4)
# creates the adjacency matrix using the constructAdjacencyMatrix method
# and prints the (0,0) and (0,1) graph nodes adjacencies
matrix_test = seg.constructAdjacencyMatrix(image)
print(matrix_test[0])
print(matrix_test[1])

# creates black and white version of segmented_image_matrix to display
out_image  = np.zeros([n,n,3])
for i1 in range(n):
    for i2 in range(n):
        if segmented_image_matrix[i1][i2] != 0:
            out_image[i1][i2] = [1,1,1]
        else:
            out_image[i1][i2] = [0,0,0]

# create plot that shows the input image next to the output image using matplotlib
fig, axs = plt.subplots(1,2)
fig.suptitle('Input and segmentation')
# input image
axs[0].imshow(image)
axs[0].set_title(f"Input image ({n}x{n})")
# output image
axs[1].imshow(out_image)
axs[1].set_title("Binary segmentation")
plt.show()