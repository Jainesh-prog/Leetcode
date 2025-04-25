class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # key -> node

        # Dummy head and tail
        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        # Connect dummy head and tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node):
        # Remove a node from the DLL
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def _insert_at_head(self, node):
        # Insert node right after head (most recently used)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            # Move to front
            self._remove(node)
            self._insert_at_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self._remove(self.cache[key])

        # Insert new node
        node = Node(key, value)
        self.cache[key] = node
        self._insert_at_head(node)

        if len(self.cache) > self.capacity:
            # Remove LRU node (just before dummy tail)
            lru = self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]
