import sys

class Vector:
    def __init__(self, *args):
        if len(args) == 0 or len(args) >2:
            sys.exit("Wrong Parameters")
        if len(args) == 1:
            value = args[0]
            if type(value) == type([0, 1, 2, 3]):
                i = len(value) - 1
                while i >= 0:
                    value[i] = float(value[i])
                    i -=1
            elif (type(value) == int):
                i = 0
                tab = []
                while (i < value):
                    tab.append(float(i))
                    i += 1
                value = tab
            else:
                sys.exit("Wrong Parameters")
        if len(args) == 2:
            if type(args[0]) != int or type(args[1]) != int:
                sys.exit("Wrong Parameters")
            begin = args[0]
            end = args[1]
            tab = []
            i = 0
            if begin == end:
                sys.exit("Wrong Parameters")
            if begin < end:
                while begin < end:
                    tab.append(float(begin))
                    i += 1
                    begin += 1
            else:
                while begin > end:
                    tab.append(float(begin))
                    i += 1
                    begin -= 1
            value = tab
        self.coordinates = value
    
    def __add__(self, scalar):
        print("here")
        if type(scalar) != int and type(scalar) != float and type(scalar) != Vector:
                print("Warning : Addition can only be perform with a scalar or a vector")
                #return Vector(for i in self: i + scalar)
        if type(scalar) == int or type(scalar) == float:
            i = len(self.coordinates) - 1
            while (i >= 0):
                self.coordinates[i] = self.coordinates[i] + scalar
                i -= 1
        else:
            i = min(len(self.coordinates), len(scalar.coordinates)) - 1
            while i >= 0:
                self.coordinates[i] = self.coordinates[i] + scalar.coordinates[i]
                i -=1

    def __sub__(self, scalar):
        if type(scalar) != int and type(scalar) != float and type(scalar) != Vector:
                print("Warning : Substraction can only be perform with a scalar or a vector")
                return
        if type(scalar) == int or type(scalar) == float:
            i = len(self.coordinates) - 1
            while (i >= 0):
                self.coordinates[i] = self.coordinates[i] - scalar
                i -= 1
        else:
            i = min(len(self.coordinates), len(scalar.coordinates)) - 1
            while i >= 0:
                self.coordinates[i] = self.coordinates[i] - scalar.coordinates[i]
                i -=1

    def __truediv__(self, scalar):
        print("la")
        if type(scalar) != int and type(scalar) != float:
                print("Warning : Division can only be perform with a scalar")
                return
        if scalar == 0:
                print("Warning : Cannot divide by 0")
                return
        i = len(self.coordinates) - 1
        while (i >= 0):
            self.coordinates[i] = self.coordinates[i] / scalar
            i -= 1

    def __mul__(self, scalar):
        if type(scalar) != int and type(scalar) != float and type(scalar) != Vector:
                print("Warning : Multiplication can only be perform with a scalar or a vector")
                return
        if type(scalar) == int or type(scalar) == float:
            i = len(self.coordinates) - 1
            while (i >= 0):
                self.coordinates[i] = self.coordinates[i] * scalar
                i -= 1
        else:
            i = min(len(self.coordinates), len(scalar.coordinates)) - 1
            while i >= 0:
                self.coordinates[i] = self.coordinates[i] * scalar.coordinates[i]
                i -=1
