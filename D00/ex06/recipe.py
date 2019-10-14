import sys
cookbook = {'sandwich':{'ingredients':['ham', 'bread', 'cheese', 'tomatoes'], 'meal':'lunch', 'prep_time':10},
            'cake':{'ingredients':['flour', 'sugar', 'eggs'], 'meal':'lunch', 'prep_time':60},
            'salad':{'ingredients':['avocado', 'arugula', 'tomatoes', 'spinach'], 'meal':'lunch', 'prep_time':15}}
#for key, values in cookbook.items():
    #print(key, values)
def print_recipe(name_of_recipe):
    print("Recipe for " + name_of_recipe + ":")
    print("Ingredients list: {}".format(cookbook[name_of_recipe]['ingredients']))
    print("To be eaten for " + cookbook[name_of_recipe]['meal'])
    print("Takes {} minutes of cooking.".format(cookbook[name_of_recipe]['prep_time']))
    print("")
    return

def delete_recipe(name_of_recipe):
    del(cookbook[name_of_recipe])
    print("")
    return 

def add_recipe(name_of_recipe, ingredients, meal, prep_time):
    cookbook.update({name_of_recipe : {'ingredients':ingredients, 'meal':meal, 'prep_time':prep_time}})
    print("")
    return

def print_recipes():
    for key, values in cookbook.items():
        print(key)
    print("")
    return
list = [add_recipe, delete_recipe, print_recipe, print_recipes]
to_display_1 = """Please select an option by typing the corresponding number:
   1: Add a recipe
   2: Delete a recipe
   3: Print a recipe
   4: Print the cookbook
   5: Quit
   """
while 1:
    func = int(input(to_display_1))
    print("")
    if (func == 5):
        sys.exit()
    elif (func == 1):
        recipe = input("Please enter the new recipe's name: ")
        print("")
        ingredients = input("Please enter the new recipe's ingredients according to the following format : [ingredient_1, ingredient_2, ...]: ")
        print("")
        meal = input("Please enter the best meal to eat the new recipe: ")
        print("")
        prep_time = input("Please enter the time to cook the new recipe: ")
        print("")
        list[func - 1](recipe, ingredients, meal, prep_time)
    elif (func == 4):
        list[func - 1]()
    elif (func == 3):
        recipe = input("Please enter the recipe's name to get details: ")
        if recipe not in cookbook:
            print("This recipe does not exist.")
        else:
            list[func - 1](recipe)
    elif (func == 2):
        recipe = input("Please enter the recipe's name you want to delete: ")
        if recipe not in cookbook:
            print("This recipe does not exist.")
        else:
            list[func - 1](recipe)