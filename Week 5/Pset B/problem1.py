"""
problem 1 is alone because it's very different from rest

    Problem 1: Mutual Friends

    Questions i would ask:
    1. do we compare based on name or object reference? like if two villagers have same name but are diff objects?
    2. should the order of the mutual list matter?

    pseudocode:
    - loop through this villager's friends
    - if that friend also appears in new_contact.friends then add friend.name to result list
    - return the list
    """
class Villager:
    

    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        mutuals = []
        for friend in self.friends:
            if friend in new_contact.friends:
                mutuals.append(friend.name)
        return mutuals


# testcases
bob = Villager("Bob", "Cat", "pthhhpth")
marshal = Villager("Marshal", "Squirrel", "sulky")
ankha = Villager("Ankha", "Cat", "me meow")
fauna = Villager("Fauna", "Deer", "dearie")
raymond = Villager("Raymond", "Cat", "crisp")
stitches = Villager("Stitches", "Cub", "stuffin")

bob.friends = [stitches, raymond, fauna]
marshal.friends = [raymond, ankha, fauna]
print(bob.get_mutuals(marshal))  

ankha.friends = [marshal]
print(bob.get_mutuals(ankha))    
