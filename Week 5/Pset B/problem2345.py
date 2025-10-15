# rest of the problems 


"""
NOTE: Problems 2–5 are all about Linked Lists.
This file defines a single Node class with methods to perform:
- insert at head
- insert at tail
- delete a node
- print the list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    """
    Problem 2: Insert at Head
    
    Questions:
    1. should the new node always become the new head?
    2. how do we handle an empty list?
    3. do we return the new head each time?

    Pseudocode:
    - make new node with value
    - point new node.next to current head
    - return new node as new head
    """
    
    def insert_at_head(self, head, value):
        new_node = Node(value)
        new_node.next = head
        return new_node

    """
    Problem 3: Insert at Tail
    
    Questions:
    1. how do we handle empty list (head = None)?
    2. should we traverse until the last node or keep a tail pointer?
    3. do we return head again after insertion?

    Pseudocode:
    - create new node
    - if head is None, return new node
    - traverse to last node
    - set last.next = new node
    - return head
    """
    def insert_at_tail(self, head, value):
        new_node = Node(value)
        if head is None:
            return new_node
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        return head

    """
    Problem 4: Delete Node
    
    Questions:
    1. what if the value isn’t found?
    2. what if it’s the head node?
    3. should we delete only the first occurrence?

    Pseudocode:
    - if list empty, return None
    - if head matches, return head.next
    - else traverse keeping track of prev
    - if found, remove by linking prev.next to curr.next
    - return head
    """
    
    def delete_node(self, head, value):
        if head is None:
            return None
        if head.value == value:
            return head.next
        prev = None
        curr = head
        while curr and curr.value != value:
            prev = curr
            curr = curr.next
        if curr:
            prev.next = curr.next
        return head
    """
    Problem 5: Print List
    
    Questions:
    1. how should we format the print? (e.g., arrows)
    2. what if list is empty?
    3. should we return string or just print?

    Pseudocode:
    - start from head
    - while curr not None:
        print curr.value + " -> "
        move curr forward
    - print "None" at the end
    """
    
    def print_list(self, head):
        curr = head
        while curr:
            print(curr.value, end=" -> ")
            curr = curr.next
        print("None")

# TEST CASES FOR PROBLEMS 2–5


temp = Node(0)
head = None

# Problem 2
head = temp.insert_at_head(head, 10)
head = temp.insert_at_head(head, 20)
head = temp.insert_at_head(head, 30)
print("After insert_at_head:")
temp.print_list(head)

# Problem 3
head = temp.insert_at_tail(head, 5)
head = temp.insert_at_tail(head, 1)
print("After insert_at_tail:")
temp.print_list(head) 

# Problem 4
head = temp.delete_node(head, 20)
head = temp.delete_node(head, 1)
print("After delete_node:")
temp.print_list(head)  

# Problem 5
print("Final list:")
temp.print_list(head)
