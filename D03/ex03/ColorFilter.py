import sys
import numpy as np
sys.path.insert(1, '../ex01')
from ImageProcessor import ImageProcessor

class ColorFilter:
    def invert(self, array):
        for i in range(0,array.shape[0]):
            for j in range(0, array.shape[1]):
                array[i][j] = [1,1,1] - arr[i][j]
        return(array)
    
    def to_green(self, array):
        ret = np.zeros(array.shape)
        for i in range(0,array.shape[0]):
            for j in range(0, array.shape[1]):
                ret[i][j] = [array[i][j][0], array[i][j][1], 0]
        return(ret)

    def to_red(self, array):
        ret = array *[1,0,1]
        return(ret)
    
    def to_blue(self, array):
        ret = array *[0,1,1]
        return(ret)

    def to_greyscale(self, array, filter='m'):
        ret = np.zeros(array.shape)
        for i in range(0,array.shape[0]):
            for j in range(0, array.shape[1]):
                if filter == 'm':
                    e = (array[i][j][0] + array[i][j][1] + array[i][j][2]) / 3
                else:
                    e = (0.299 * array[i][j][0] + 0.587 * array[i][j][1] + 0.114 * array[i][j][2]) 
                ret[i][j] = e * array[i][j]
        return(ret)

imp = ImageProcessor()
arr = imp.load("../42AI.png")
cf = ColorFilter()
tab = cf.to_greyscale(arr)
imp.display(tab)