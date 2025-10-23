class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

"""
Problem 1: Wild Goose Chase

Pseudocode:
Follow the list until the end and just check if the last node points back to the start.  

Two Questions:
Do we count it as circular only if it loops exactly to the head?  
What if the list is empty, should that count as circular or not?

Time: O(n)
Space: O(1)
"""
def is_circular(clues):
    
    if not clues:
        return False

    current = clues.next
    while current and current != clues:
        current = current.next

    return current == clues




"""
Problem 2: Breaking the Cycle

Pseudocode:
Use two pointers to find where the list loops, then walk through that loop and grab all the values inside it.  

Two Questions:
Should I return duplicates if the loop circles back through them again?  
And if there’s no cycle at all, should I just return an empty list?

Time: O(n)
Space: O(1)
"""

def collect_false_evidence(evidence):
    
    def get_cycle_node(head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow
        return None

    cycle_node = get_cycle_node(evidence)
    if not cycle_node:
        return []

    result = []
    start = cycle_node
    while True:
        result.append(start.value)
        start = start.next
        if start == cycle_node:
            break
    return result


"""
Problem 3: Prioritizing Suspects

Pseudocode:
Go through the list and separate suspects into two groups based on the threshold, then link those groups together.  

Two Questions:
Do the suspects in each group have to stay in their original order?  
And if all values are below the threshold, do we just return the same list?

Time: O(n)
Space: O(1)
"""

def partition(suspect_ratings, threshold):
    
    greater_head = greater_tail = Node(0)
    lesser_head = lesser_tail = Node(0)
    current = suspect_ratings

    while current:
        if current.value > threshold:
            greater_tail.next = current
            greater_tail = greater_tail.next
        else:
            lesser_tail.next = current
            lesser_tail = lesser_tail.next
        current = current.next

    greater_tail.next = lesser_head.next
    lesser_tail.next = None
    return greater_head.next


"""
Problem 4: Puzzling it Out

Pseudocode:
Compare both lists one node at a time, always picking the smaller value first and stitching them together.  

Two Questions:
If both values are equal, does it matter which list’s node goes first?  
Should I build a new list or just reuse the old nodes?

Time: O(n + m)
Space: O(1)
"""

def merge_timelines(known_timeline, witness_timeline):
    
    dummy = Node(0)
    tail = dummy

    while known_timeline and witness_timeline:
        if known_timeline.value <= witness_timeline.value:
            tail.next = known_timeline
            known_timeline = known_timeline.next
        else:
            tail.next = witness_timeline
            witness_timeline = witness_timeline.next
        tail = tail.next

    tail.next = known_timeline or witness_timeline
    return dummy.next


"""
Problem 5: A New Perspective

Pseudocode:
Find how long the list is, link the end to the head to make it circular, then break it at the new rotation point.  

Two Questions:
If k is bigger than the list length, should we rotate it modulo the length?  
And if k is zero, should I just return the list as is?

Time: O(n)
Space: O(1)

"""

def rotate_right(evidence, k):
    
    if not evidence or k == 0:
        return evidence

    length = 1
    tail = evidence
    while tail.next:
        tail = tail.next
        length += 1

    k %= length
    if k == 0:
        return evidence

    tail.next = evidence
    steps_to_new_head = length - k
    new_tail = evidence

    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None
    return new_head


#testcases

clue1 = Node("The stolen goods are at an abandoned warehouse")
clue2 = Node("The mayor is accepting bribes")
clue3 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue1
print(is_circular(clue1))

clue1 = Node("Unmarked sedan seen near the crime scene")
clue2 = Node("The stolen goods are at an abandoned warehouse")
clue3 = Node("The mayor is accepting bribes")
clue4 = Node("They dumped their disguise in the lake")
clue1.next = clue2
clue2.next = clue3
clue3.next = clue4
clue4.next = clue2
clue5 = Node("A masked figure was seen fleeing the scene")
clue6 = Node("Footprints lead to the nearby woods")
clue7 = Node("A broken window was found at the back")
clue5.next = clue6
clue6.next = clue7
print(collect_false_evidence(clue1))
print(collect_false_evidence(clue5))

suspect_ratings = Node(1, Node(4, Node(3, Node(2, Node(5, Node(2))))))
print_linked_list(partition(suspect_ratings, 3))

known_timeline = Node(1, Node(2, Node(4)))
witness_timeline = Node(1, Node(3, Node(4)))
print_linked_list(merge_timelines(known_timeline, witness_timeline))

evidence_list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
evidence_list2 = Node(0, Node(1, Node(2)))
print_linked_list(rotate_right(evidence_list1, 2))
print_linked_list(rotate_right(evidence_list2, 4))