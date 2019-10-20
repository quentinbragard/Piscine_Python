import sys

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.type = type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt ="""Name : {}
Cooking Level : {}
Cooking Time : {}
Ingredients : {}
Description : {}
Type : {} """.format(self.name, self.cooking_lvl, self.cooking_time, self.ingredients, self.description, self.type) 
        return txt


    def __setattr__(self, name, value):
        if name == "name":
            if type(value) != type("str"):
                sys.exit('Error : The name of your recipe must be a text. Use "" when typing it.')
            if len(value) <= 0:
                sys.exit("Error : You must define a name for your recipe.")
            super(Recipe, self).__setattr__(name, value)
        if name == "cooking_lvl":
            if type(value) != type(1):
                sys.exit('Error : The Cooking Level of your recipe must be an integer. Do not use "" when typing it.')
            if value <= 0 or value > 5:
                sys.exit("Error : The Cooking Level must be an integer in the range 1-5.")
            super(Recipe, self).__setattr__(name, value)
        if name == "cooking_time":
            if value < 0:
                sys.exit("Error : The Cooking Time must be a positive or null integer.")
            super(Recipe, self).__setattr__(name, value)
        if name == "ingredients":
            if not isinstance(value, list):
                sys.exit("Error : The ingredients must be written in a list. Use () when typing them.")
            super(Recipe, self).__setattr__(name, value)
        if name == "description":
            if type(value) != type("str") and value != None:
                sys.exit('Error : The description of your recipe must be a text. Use "" when typing it.')
            super(Recipe, self).__setattr__(name, value)
        if name == "type":
            if value != "starter" and value != "main_course" and value != "dessert":
                sys.exit('Error : The value can only be "starter", "main_course" or "dessert".')
            super(Recipe, self).__setattr__(name, value)