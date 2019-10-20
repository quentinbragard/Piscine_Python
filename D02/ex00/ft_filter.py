def test(x):
    if x > 18:
        return (True)
    return (False)

def test2(c):
    if c.isupper():
        return (True)
    return (False)


def ft_filter(f, to_filter):
    result = []
    for elem in to_filter:
        if f(elem) == True:
            result.append(elem) 
    return (result)

ages = "Hello FRIENDS"
majeurs = filter(test2, ages)
ft_majeurs = ft_filter(test2, ages)
for age in majeurs:
    print(age)
print("")
for ft_age in ft_majeurs:
    print(ft_age)
