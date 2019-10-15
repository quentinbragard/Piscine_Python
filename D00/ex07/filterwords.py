import sys
import re
import string
if len(sys.argv) != 3:
    print("ERROR")
    sys.exit()
str = sys.argv[1]
max_size = sys.argv[2]
if str.isnumeric():
    print("ERROR")
    sys.exit()
if max_size.isnumeric() == False:
    print("ERROR")
    sys.exit()
for c in str:
    if c in string.punctuation:
        str = str.replace(c, ' ')
str = str.split()
i = 0
end = len(str)
while i < end:
    if len(str[i]) <= int(max_size):
        del str[i]
        i  = -1
        end -= 1  
    i += 1
print(str)
        
        
