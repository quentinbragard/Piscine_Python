
def ft_map(f, list):
    result = []
    for elem in list:
        result.append(f(elem))
    return (result)


def test(str):
    result = ""
    for c in str:
        result += 'a'
    return (result)
memes = ["It's over 9000 !", "All your base are belong to us."]
result = map(test, memes)
for elem in result:
    print(elem)
print("")
result2 = ft_map(test, memes)
for elem2 in result2:
    print(elem2)