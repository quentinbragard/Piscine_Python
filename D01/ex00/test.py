from book import *


cheescake = Recipe("cheesecake", 1, 20, ("cheese", "cake"), "12", "starter")
applecake = Recipe("applecake", 3, 50, ("apple", "cake"), "15", "starter")
bouquin = Book("mdr", {"starter":cheescake})
print(cheescake.name)
print(cheescake.cooking_lvl)
print(cheescake.cooking_time)
print(cheescake.ingredients)
print(cheescake.description)
print(cheescake.type)
print(bouquin.name)
bouquin.name = "en fait lol ahah"
print(bouquin.name)
print(bouquin.creation_date)
print(bouquin.last_update)
bouquin.get_recipe_by_name("cheesecake")
print(cheescake.__dict__)
