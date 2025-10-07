"""
Questions I would ask:
1. can tags be nested arbitrarily?
2. assume tags are well-formed?
3. what if empty string?

Plan in plain english:
loop through the html string char by char, when < found, read until > to get tag, push opening tags onto stack, pop when closing tags match, if mismatch return False, return True if stack empty at end
"""

def validate_html_tags(html):
 stack = []
 i = 0
 n = len(html)
 while i < n:
  if html[i] == '<':
   j = i+1
   while j < n and html[j] != '>':
    j += 1
   if j == n: return False
   tag = html[i+1:j]
   if not tag.startswith('/'):
    stack.append(tag)
   else:
    if not stack or stack[-1] != tag[1:]:
     return False
    stack.pop()
   i = j
  i += 1
 return len(stack) == 0

html="<div><p></p></div>"
print(validate_html_tags(html))
html_2="<div><p></div></p>"
print(validate_html_tags(html_2))
html_3="<div><p><a></a></p></div>"
print(validate_html_tags(html_3))
html_4="<div><p></a></p></div>"
print(validate_html_tags(html_4))

#time complexity: O(n)
#space complexity: O(m)
