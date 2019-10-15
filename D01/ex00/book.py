from recipy import *
import datetime

class Book:
    def __init__(self, name, recipes_list):
        self.name = name
        self.recipes_list = recipes_list

    def _get_creation_date(self):
        return self._creation_date

    def _get_last_update(self):
        return self._last_update

    
    def __setattr__(self, name, value):
        if name == "name":
            if type(value) != type("str"):
                sys.exit('Error : The name of your book must be a text. Use "" when typing it.')
            if len(value) <= 0:
                sys.exit("Error : You must define a name for your book.")
            self._creation_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self._last_update = self._creation_date
        if name == "recipes_list":
            if type(value) != type({"str":"str"}):
                sys.exit("Error : You must define a dictionnary for your recipes list.")
        super(Book, self).__setattr__(name, value)

    creation_date = property(_get_creation_date)
    last_update = property(_get_last_update)

    def get_recipe_by_name(self, name):
        found = 0
        for item in self.recipes_list:
            if self.recipes_list[item].name == name:
                print(self.recipes_list[item])
                found = 1
        if found == 0:
            print("Error: This recipe does nos exist")