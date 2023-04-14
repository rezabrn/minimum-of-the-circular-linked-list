import Node

class CircularLinkedList:
    def __init__(self):
        self.head = Node.Node(None)
        self.head.next = self.head
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_first(self, data):
        new_node = Node.Node(data)
        if self.is_empty():
            self.head.next = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head.next
            self.head.next = new_node
        self.size += 1
    
    def add_last(self, data):
        new_node = Node.Node(data)
        if self.is_empty():
            self.head.next = new_node
            new_node.next = self.head
        else:
            current = self.head.next
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        self.size += 1
    
    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            self.head.next = self.head.next.next
            self.size -= 1
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            current = self.head.next
            while current.next.next != self.head:
                current = current.next
            current.next = self.head
            self.size -= 1
    
    def search(self, data):
        current = self.head.next
        for i in range(self.size):
            if current.data == data:
                return i
            current = current.next
        return -1