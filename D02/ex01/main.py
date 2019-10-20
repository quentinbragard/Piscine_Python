def what_are_the_vars(*args, **kwargs):
    obj = ObjectC()
    i = 0
    for elem in args:
        setattr(obj, "var_"+str(i), elem)
        i += 1
    for elem in kwargs:
        if hasattr(obj, elem) == True:
            exit("Error")
        setattr(obj, elem, kwargs[elem])
    return (obj)
    
class ObjectC(object):
    def __init__(self):
        pass

def doom_printer(obj):
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

obj = what_are_the_vars(7)
doom_printer(obj)
obj = what_are_the_vars("ft_lol", "Hi")
doom_printer(obj)
obj = what_are_the_vars()
doom_printer(obj)
obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
doom_printer(obj)
obj = what_are_the_vars(42, a=10, var_0="world")
doom_printer(obj)