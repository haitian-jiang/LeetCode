# medium
'''2022-01-16'''

class Node():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache():
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        curr = self.map[key]
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        curr.next = self.tail
        curr.prev = self.tail.prev
        self.tail.prev.next = curr
        self.tail.prev = curr
        return curr.value


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            curr = self.map[key]
            curr.value = value
            curr.next.prev = curr.prev
            curr.prev.next = curr.next
        else:
            curr = Node(key, value)
            self.map[key] = curr

        # insert
        curr.next = self.tail
        curr.prev = self.tail.prev
        self.tail.prev.next = curr
        self.tail.prev = curr

        # remove if needed
        if len(self.map) > self.capacity:
            remove = self.head.next
            self.map.pop(remove.key)
            self.head.next = remove.next
            remove.next.prev = self.head
            del remove
