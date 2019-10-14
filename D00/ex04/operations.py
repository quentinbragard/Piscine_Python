import sys
error = """Usage: python operations.py <number1> <number2>
Example: python operations.py 10 3"""
if len(sys.argv) != 3:
    print(error)
    sys.exit()
if sys.argv[1].isnumeric() == False or sys.argv[2].isnumeric() == False:
    print(error)
    sys.exit()
number1 = int(sys.argv[1])
number2 = int(sys.argv[2])

print("Sum:         {}".format(number1 + number2))
print("Difference:  {}".format(number1 - number2))
print("Product:     {}".format(number1 * number2))
if number2 == 0:
    print("Quotient:    0")
    print("Remainder:   0")
else:
    print("Quotient:    {}".format(number1 / number2))
    print("Remainder:   {}".format(number1 % number2))
 