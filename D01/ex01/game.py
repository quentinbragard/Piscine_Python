import sys

class GotCharacter:
    def __init__(self, first_name):
        self.first_name = first_name
        self.is_alive = True

class Stark(GotCharacter):
    """A class representing the Stark family. Not bad people but a lot of bad luck."""
    def __init__(self, first_name):
        super().__init__(first_name=first_name)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"
    def print_house_words(self):
        print(self.house_words)
    def die(self):
        self.is_alive = False


arya = Stark("Arya")
print(arya.__dict__)
arya.print_house_words()
print(arya.is_alive)
arya.die()
print(arya.is_alive)
print(arya.__doc__)