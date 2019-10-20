import numpy as np
import matplotlib.pyplot as plt

class ImageProcessor:
    def load(self, path):
        img = plt.imread(path)
        array = np.array(img, dtype = float)
        print("Loading image of dimensions " + str(array.shape[0]) + "x" + str(array.shape[1]))
        return (array)
    def display(self, arr):
        plt.imshow(arr)
        plt.show()
