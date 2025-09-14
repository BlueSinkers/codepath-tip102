
"""
Questions I would ask to help understand question:
1. How do I determine the words to reverse the list?
2. What do I do with the reversed list?

Plan in plain English (pseudocode):
Use split function to split the input into a list of words. Reverse the list using slicing. Join the reversed list into a string with spaces in between and return it.

Begin problem:
"""

def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

sentence = "tubby little cubby all stuffed with fluff"
print(reverse_sentence(sentence))

sentence = "Pooh"
print(reverse_sentence(sentence))
