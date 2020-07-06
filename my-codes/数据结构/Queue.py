from SinglyLinkedList import SinglyLinkedList

class Queue:
    """use singly-linked list to impliment"""
    def __init__(self, *args):
        self.__instance = SinglyLinkedList(*args)
        self.front = self.rear = None
        if self.__instance:
            self.front = self.__instance.head.next.value
            self.rear = self.__instance.tail.value
    
    def __len__(self):
        return self.__instance.length

    def is_empty(self):
        return self.__instance.is_empty()

    def enqueue(self, value):
        self.__instance.append(value)
        self.front = self.__instance.head.next.value
        self.rear = self.__instance.tail.value
    
    def dequeue(self):
        self.__instance.pop()
        self.front = self.rear = None
        if self.__instance:
            self.front = self.__instance.head.next.value
            self.rear = self.__instance.tail.value


if __name__ == "__main__":
    a = Queue()
    a.enqueue(1)
    print(a.front, a.rear)
    a.enqueue(3)
    print(a.front, a.rear)
    a.enqueue(7)
    print(a.front, a.rear)
    a.dequeue()
    print(a.front, a.rear)
    a.dequeue()
    print(a.front, a.rear)
    a.dequeue()
    print(a.front, a.rear)
    print(a.is_empty())