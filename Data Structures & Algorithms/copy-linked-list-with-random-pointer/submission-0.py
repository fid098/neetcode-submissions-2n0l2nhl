"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        given the head with lenght n
        each node contains a pointer that points to any node or null
        we could use a hashmap to store the nodes and their values and randoms
        or
        
        """

        if not head:
            return None
        
        old_to_new = {}
        current = head

        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        return old_to_new[head]
        
