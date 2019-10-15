import sys
import random

def generator(text, **kwargs):  
    if "sep"  not in kwargs:
        sep = " "
    else:
        sep = kwargs['sep']
    tab = text.split(sep)
    if "option" in kwargs:
        option = kwargs['option']
        if option != "shuffle" and option != "unique" and option != "ordered":
            sys.exit("Selected Option does not exist")
        elif option == "shuffle":
            random.shuffle(tab)
        elif option == "unique":
            tab = list(dict.fromkeys(tab))
        else:
            tab.sort(reverse=True)

    
    for elem in tab:
        print(elem)
  
# Driver code 
text = "Le Lorem Ipsum est simplement du faux texte."
generator(text, sep=" ", option="ordered") 

   # for key, value in kwargs.items(): 
   #     print ("%s == %s" %(key, value))
   # print(text)
   # print(kwargs['first']) 