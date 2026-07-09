class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node("head", "head")
        self.tail = Node("tail", "tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def add(self, node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            tail = self.tail.prev
            self.remove(tail)
            del self.cache[tail.key]
        
