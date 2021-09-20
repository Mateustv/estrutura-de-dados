class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        self._head = Node(None)

    def insert_node_to_tail(self, node):
        self.tail().next(node)

    def insert_node_to_head(self, node):
        if self._head.next:
            node.next, self._head = self._head.next, node
        self._head.next(node)

    def is_empty(self):
        return self._head.next is None

    def head(self):
        return self._head.next

    def tail(self):
        while self._head.next:
            current = self._head.value
        return current
