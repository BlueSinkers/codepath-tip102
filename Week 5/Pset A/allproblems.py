"""
NOTE: all problems are in the same file for ease of submission because all use same class


"""

class Villager:
    
    """ 
    Problem 1: New Horizons

    Questions I would ask:
    1. are we just making one villager or do we need like a list of them later?
    2. should furniture always start empty or can we pass it in?

    pseudocode:
    - make class with init, assign name/species/catchphrase
    - set furniture to empty list
    - make apollo villager and print out fields
    """
    
    
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []
        
    """
    Problem 2: Greet Player

    Questions:
    1. can player_name be empty? what happens then?
    2. is greet supposed to always have the same structure?

    pseudocode:
    - create bones villager
    - call greet_player with my name and print
    """
    
    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"
    """
    Problem 3: Update Catchphrase

    Questions:
    1. do we directly modify attribute or use a setter here?
    2. is there any rule about formatting the new phrase?

    pseudocode:
    - set bones.catchphrase manually
    - print greet again with new phrase
    """
    
    
    """
    Problem 4: Set Catchphrase

    Questions:
    1. do we need to return anything from setter or just print?
    2. what about edge length exactly 20?

    pseudocode:
    - make alice villager
    - call set_catchphrase with valid string and print attribute
    - call with invalid string and check that old one stays
    """
    
    def set_catchphrase(self, new_catchphrase):
        if len(new_catchphrase) < 20 and all(c.isalpha() or c.isspace() for c in new_catchphrase):
            self.catchphrase = new_catchphrase
            print("Catchphrase Updated!")
        else:
            print("Invalid catchphrase")

    """
    Problem 5: Add Furniture

    Questions:
    1. can we add the same thing twice? is that allowed?
    2. should casing matter when matching items?

    pseudocode:
    - test add_item with a few valid and invalid items
    - print furniture each time to check if it updated
    """

    def add_item(self, item_name):
        valid_items = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid_items:
            self.furniture.append(item_name)

#problem 1 testcases
apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)
print(apollo.species)
print(apollo.catchphrase)
print(apollo.furniture)


# problem 2 testcases
bones = Villager("Bones", "Dog", "yip yip")
print(bones.greet_player("Abhiram"))



# problem 3 testcases
bones.catchphrase = "ruff it up"
print(bones.greet_player("Samia"))


# problem 4 testcases
alice = Villager("Alice", "Koala", "guvnor")
alice.set_catchphrase("sweet dreams")
print(alice.catchphrase)
alice.set_catchphrase("#?!")
print(alice.catchphrase)


# problem 5 testcases

alice = Villager("Alice", "Koala", "guvnor")
print(alice.furniture)
alice.add_item("acoustic guitar")
print(alice.furniture)
alice.add_item("cacao tree")
print(alice.furniture)
alice.add_item("nintendo switch")
print(alice.furniture)
