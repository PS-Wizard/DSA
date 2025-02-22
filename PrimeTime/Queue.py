class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def enqueue(self, value):
        new_node = Node(value)
        if not self.tail:  
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def dequeue(self):
        if not self.head:
            return None  
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None  
        self.length -= 1
        return value

    def peek(self):
        return self.head.value if self.head else None

    def is_empty(self):
        return self.length == 0

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <- ".join(values)
