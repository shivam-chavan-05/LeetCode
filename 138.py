# Copy List with Random Pointer

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
        if not head:
            return None

        curr = head
        hashmap = {}

        while curr:
            node = Node(x = curr.val)
            hashmap[curr] = node
            curr = curr.next

        curr = head
        while curr:
            new_node = hashmap[curr]
            new_node.next = hashmap[curr.next] if curr.next else None
            new_node.random = hashmap[curr.random] if curr.random else None
            curr = curr.next

        return hashmap[head]
