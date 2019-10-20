import sys
import numpy as np
sys.path.insert(1, '../ex01')
from ImageProcessor import ImageProcessor

class ScrapBooker:
    def crop(self, array, dimensions, position=([0,0])):
        return (array[position[0]:position[0] + dimensions[0], position[1]:position[1] + dimensions[1]])
    def thin(self, array, n, axis):
        return(np.delete(array,n, axis))
    def juxtapose(self, array, n, axis):
        if n <= 0:
            exit
        array2 = array
        for i in range(1,n):
            array2 = np.concatenate((array2, array), axis)
        return (array2)
    def mosaic(self, array, dimensions):
        if array.shape[0] == 0 or array.shape[1] == 0:
            exit
        x = int(round(max(dimensions[0] / array.shape[0], dimensions[1] / array.shape[1]),0))
        array2 = np.tile(array, [x,x,1 ])
        if dimensions[0] - array2.shape[0] > 0:
            array3 = scp.crop(array2,[dimensions[0] - array2.shape[0],array2.shape[1]])
            array2 = np.concatenate((array2, array3), 0)
        if dimensions[1] - array2.shape[1] > 0:
            array3 = scp.crop(array2,[array2.shape[0],dimensions[1] - array2.shape[1]])
            array2 = np.concatenate((array2, array3), 1)        
        return(array2)


imp = ImageProcessor()
scp = ScrapBooker()
arr = imp.load("../42AI.png")


















#dimensions = [20,167]
#position = [139,16]
#arr2 = scp.crop(arr, dimensions, position)

#arr2 = scp.thin(arr, 200, 1)

#for i in range(125,175):
#    arr2 = scp.thin(arr, 125, 1)
#    arr = arr2


#arr2 = scp.juxtapose(arr, 4, 0)

#arr2 = scp.mosaic(arr, [4780, 450])
#imp.display(arr2)


#arr = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]], [[13,14,15], [16,17,18], [19,20,21], [22,23,24]], [[25,26,27], [28,29,30], [31,32,33], [34,35,36]], [[37,38,39], [40,41,42], [43,44,45], [46,47,48]]])
#arr2 = arr[2:3, 0:4]
#print(arr2)


