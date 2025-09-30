
"""
Questions I would ask to help understand question:
1. Why do I use a stack here?
2. What happens for empty list?

Plan in plain English (pseudocode):
I will load all of these into a stack. Then, I will continually pop the stack which returns the list in reveresd order.

Begin problem:
"""

def reverse_comments_queue(comments):
    stack = [] 
    for comment in comments:
        stack.append(comment)
    
    for i in range(len(comments)):
        comments[i] = stack.pop()
    
    return comments 

print(reverse_comments_queue(["Great post!", "Love it!", "Thanks for sharing."]))

print(reverse_comments_queue(["First!", "Interesting read.", "Well written."]))