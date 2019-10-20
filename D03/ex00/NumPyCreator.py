import numpy as np

class NumPyCreator:
    def from_list(self, list, type=int):
        return(np.int8(np.array(list, dtype = type)))
    def from_tuple(self, tuple, type=str):
        return(np.array(tuple, dtype = type))
    def from_iterable(self, iterable, type=int):
        return(np.array(iterable, dtype = type))
    def from_shape(self, shape, value=0, type=int):
        return (np.full(shape, value, dtype = type))
    def random(self, shape):
        return (np.random.random(shape))
    def identity(self, n, type=int):
        return(np.identity(n, dtype = type))

