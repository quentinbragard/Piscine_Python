import sys
if len(sys.argv) != 2:
    if len(sys.argv) != 1:
        print("ERROR")
    sys.exit()
if sys.argv[1][0] == '-' or sys.argv[1][0] == '+':
    number = sys.argv[1][1:len(sys.argv[1])]
else:
    number = sys.argv[1]
if  number.isnumeric() == False:
    print("ERROR")
    sys.exit()
number = int(number)
if number == 0:
    print("I'm Zero.")
    sys.exit()
if number % 2 == 1:
    print("I'm Odd.")
    sys.exit()
else:
    print("I'm Even.")
    sys.exit()