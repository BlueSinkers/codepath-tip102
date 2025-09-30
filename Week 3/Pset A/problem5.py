
"""
Questions I would ask to help understand question:
Is this basically parens question with lower-case upper-case alphabet?
How do I deal with non-alphabet cases? What hapens if we have multiple of the same letter?

Plan in plain English (pseudocode):
Keep adding lower case values to stack. Once you get to an upper case value, pop the stack and check if the lower case value matches that value. If so, just continue. Else, add that back to the stack and the upper case value as well. At the end, take the stack and reverse it to get the final string.

Begin problem:
"""
def clean_post(post):
    stack = []
    for char in post:
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)




print(clean_post("poOost")) 
print(clean_post("abBAcC")) 
print(clean_post("s")) 