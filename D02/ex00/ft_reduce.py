import functools

def ft_reduce(f, list):
    size = len(list)
    i = 2
    result = f(list[0], list[1])
    while i < size:
        result = f(result, list[i])
        i += 1
    return (result)

def sum(a, b):
    print(str(a) + "+" +str(b) + "=" + str(a + b))
    return (a + b)
result = functools.reduce(sum, (1, 2, 50))
print(result)
print("")
result2 = ft_reduce(sum, (1, 2, 50))
print(result)