import sys
i = 1
word = ""
if len(sys.argv) < 2:
    sys.exit()
while (i < len(sys.argv)):
    j = 0
    while j < len(sys.argv[i]):
        if sys.argv[i][j].isupper():
            c = sys.argv[i][j].lower()
        else:
            c = sys.argv[i][j].upper()
        word = word + c
        j = j + 1
    i = i + 1
    if i < len(sys.argv):
        word = word + " "
print(word[::-1])

