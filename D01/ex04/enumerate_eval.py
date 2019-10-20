import sys

def enumerate_evaluate(coefs, words):
    if len(coefs) != len(words):
        return (-1)
    list = enumerate(words)
    result = 0
    for elem in list:
        result = result + (coefs[int(elem[0])] * float(len(elem[1])))
    return (result)

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]

print(enumerate_evaluate(coefs, words))