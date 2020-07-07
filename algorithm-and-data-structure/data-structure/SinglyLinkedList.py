from collections.abc import Iterable


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, *args):
        self.head = Node("○")  # indicates head node when be printed
        self.tail = self.head
        self.length = 0
        if len(args) == 1 and isinstance(args[0], Iterable):
            self.append_from_iterable(args[0])
        else:
            self.append_from_iterable(args)

    def __repr__(self):
        output = ''
        current = self.head
        while current.next:
            output = output + str(current.value) + ' -> '
            current = current.next
        return output + str(current.value)  # the tail node's value

    def __len__(self):
        return self.length

    def __pre_get_set_item(self, index):
        """test if index is valid and return the node to visit or change"""
        if not isinstance(index, int):
            raise IndexError('Index should be int')
        if index < 0:
            index = self.length + index
        if index >= self.length or index < 0:
            raise IndexError('Index out of range')
        current = self.head
        for step in range(index + 1):
            current = current.next
        return current

    def __getitem__(self, index):
        """index starts from 0"""
        current = self.__pre_get_set_item(index)
        return current.value

    def __setitem__(self, index, value):
        """index start from 0"""
        current = self.__pre_get_set_item(index)
        current.value = value

    def __iter__(self):
        self.__iter_pointer = self.head
        return self

    def __next__(self):
        if self.__iter_pointer.next:
            self.__iter_pointer = self.__iter_pointer.next
            return self.__iter_pointer.value
        else:
            raise StopIteration

    def is_empty(self):
        return self.head.next is None

    def append(self, value):
        new_node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

    def insert(self, position, value):
        if not isinstance(position, int):
            raise TypeError('Position should be int')
        if position < 0:
            position = self.length + position
        if position >= self.length:  # if the position is too big, insert in the tail
            return self.append(value)
        new_node = Node(value)
        current = self.head
        for step in range(position):
            current = current.next  # current points to the position before the adding position
        new_node.next = current.next
        current.next = new_node
        self.length += 1

    def append_from_iterable(self, iterable):
        if not isinstance(iterable, Iterable):
            raise TypeError('Parameter should be iterable')
        for item in iterable:
            new_node = Node(item)
            self.tail.next = new_node
            self.tail = new_node
        self.length += len(iterable)

    def extend(self, other):
        """other will be added to the end of self, and other will become empty"""
        self.tail.next = other.head.next  # concatenate two lists
        self.tail = other.tail
        self.length += other.length
        other.head.next = None  # destroy 'other' so that there is no connection between self and other

    def find(self, value):
        """:return the number of node with the value, 0 for the first, -1 if not found"""
        current = self.head.next
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def pop(self, position=0):
        if not isinstance(position, int):
            raise TypeError('Position should be int')
        if position < 0:
            position = self.length + position
        if position >= self.length or position < 0:
            raise IndexError('Index out of range')
        current = self.head
        for step in range(position):
            current = current.next  # current points to the item before the item to be deleted
        deleted_node = current.next
        current.next = deleted_node.next
        if deleted_node == self.tail:
            self.tail = current
        del deleted_node
        self.length -= 1


if __name__ == '__main__':
    a = SinglyLinkedList(range(10))           # test append_from_iterable() and __repr__()
    print('1. ', a)

    b = SinglyLinkedList(11, 12, 13, 14, 15)  # test __init__()
    print('2. ', b)

    a.extend(b)                               # test extend()
    print('3. ', a, b.is_empty())

    print('4. ', a[3], a[-3])                 # test __getitem__()

    a.insert(10, "'10'")                      # test insert()
    print('5. ', a)

    print('6. ', end=' ')                     # test __iter__() and __next__() and __length__()
    for i in a:
        print(i, end=' ')
    print(f'length={len(a)}')

    a[10] = 10                                # test __setitem__() and append()
    a.append('16')
    print('7. ', a)

    a.pop()                                   # test pop()
    print('8. ', a)

    print('9. ', a.find(13), a.find(20))             # test find()