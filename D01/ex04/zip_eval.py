import sys

def zip_evaluate(coefs, words):
    if len(coefs) != len(words):
        return (-1)
    result = 0
    list = tuple(zip(coefs, words))
    for elem in list:
        result = result + (float(elem[0]) * float(len(elem[1])))
    return (result)

print(zip_evaluate("lol", "oui"))