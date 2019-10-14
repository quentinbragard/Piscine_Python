def text_analyzer(*args):

    """This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text."""

    import string
    import sys
    if len(args) > 1:
        return
    if len(args) == 0:
        print("What is the text to analyze?")
        str = input()
    else:
        str = args[0]
    U_L = 0
    l_L = 0
    count = 0
    p = 0
    s = 0
    for c in str:
        count += 1
        if c in string.punctuation:
            p += 1
        elif c == ' ':
            s +=1
        elif c.isupper():
            U_L += 1
        elif c.islower():
            l_L +=1
    print("The text contains {} characters:".format(count))
    print("- {} upper letters".format(U_L))
    print("- {} lower letters".format(l_L))
    print("- {} punctuation marks".format(p))
    print("- {} spaces".format(s))
    return