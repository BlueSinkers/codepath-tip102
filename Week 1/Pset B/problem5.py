
"""
Questions I would ask to help understand question:
1. What do I do if I don't get one of those commands?
2. Anything else except increasing and decreasing number by 1?

Plan in plain English (pseudocode):
I will iterate through the operations and perform if statements for each value doing the appropriate action to the number.

Begin problem:
"""

def final_value_after_operations(operations):
    tigger = 1 
    for operation in operations:
        if operation == "trouncy" or operation == "pouncy":
            tigger -= 1
        elif operation == "bouncy" or operation == "flouncy":
            tigger += 1
    return tigger 

operations = ["trouncy", "flouncy", "flouncy"]
print(final_value_after_operations(operations))

operations = ["bouncy", "bouncy", "flouncy"]
print(final_value_after_operations(operations))
