"""
Questions I would ask to help understand question:
1. What happens when they're closed but not in order?
2. What happens if I have an empty string or a string with no parentheses?

Plan in plain English (pseudocode):
I will use a stack. When I find an open parantheses of any type, I will push it to the stack.
When I find a closing parantheses of any type, I will pop from the stack (LIFO), and check if it matches
the type of closing parantheses I saw. If they match until the end, the string is 
balanced. If it doesn't, then the string is not balanced.

Begin problem:
"""

def is_valid_post_format(posts):
    stack = [] 
    paren_map = {')': '(', '}': '{', ']': '['} 
    
    for char in posts:
        if char in paren_map.values():
            stack.append(char)
        elif char in paren_map.keys():  
            if not stack or stack[-1] != paren_map[char]:
                return False
            endchar = stack.pop()
            if endchar != paren_map[char]:
                return False
    return True   

print(is_valid_post_format("()"))
print(is_valid_post_format("()[]{}")) 
print(is_valid_post_format("(]"))
