
"""
Questions I would ask to help understand question:
1. What do I print per character?
2. How do I know what to print?

Plan in plain English (pseudocode):
Take the input in character and use if statements to print the correct greeting.

Begin problem:
"""

def print_catchphrase(character):
    if character == "Pooh":
        print("Oh, bother!")
    elif character == "Tigger":
        print("The wonderful thing about Tiggers is Tiggers are wonderful things!")
    elif character == "Eeyore":
        print("Thanks for noticing me.")
    elif character == "Christopher Robin":
        print("Silly old baer.")
    else:
        print("Sorry, I don't know " + character + "'s catchphrase.")

character = "Pooh"
print_catchphrase(character)

character = "Piglet"
print_catchphrase(character)