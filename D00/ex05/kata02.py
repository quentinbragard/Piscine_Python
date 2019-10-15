import datetime
t = (3, 30, 2019,9, 25)
x = datetime.datetime(t[2], t[3], t[4], t[0], t[1])
print(x.strftime("%m/%d/%Y %H:%M"))


    def get_recipe_by_name(self, name):
        found = 0
        for item in self.recipes_list:
            if self.recipes_list[item].name == name:
                print(self.recipes_list[item])
                found = 1
        if found == 0:
            print("Error: This recipe does nos exist")