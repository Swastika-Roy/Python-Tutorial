class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}
        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    @staticmethod
    def get(key):
        node = LRUCache.cache.get(key, None)
        if not node:
            return -1
        LRUCache._remove(node)
        LRUCache._insert(node)
        return node.value

    @staticmethod
    def put(key, value):
        if key in LRUCache.cache:
            node = LRUCache.cache[key]
            node.value = value
            LRUCache._remove(node)
            LRUCache._insert(node)
        else:
            if len(LRUCache.cache) == LRUCache.capacity:
                lru = LRUCache.tail.prev
                LRUCache._remove(lru)
                del LRUCache.cache[lru.key]
            node = Node(key, value)
            LRUCache._insert(node)
            LRUCache.cache[key] = node

    @staticmethod
    def _remove(node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    @staticmethod
    def _insert(node):
        node.next = LRUCache.head.next
        node.prev = LRUCache.head
        LRUCache.head.next.prev = node
        LRUCache.head.next = node
