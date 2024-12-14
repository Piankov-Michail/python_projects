class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    def push_back(self, value):
        if self.head == None or self.tail == None:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value)
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.length += 1
    def push_front(self, value):
        if self.head == None or self.tail == None:
            new_node = Node(value)
            self.head = self.tail = new_node
            self.length += 1
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
            self.length += 1
    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
        elif index == self.length:
            self.push_back(value)
        else:
            current = self.head
            while(current != None):
                if index == 0:
                    new_node = Node(value)
                    new_node.next = current
                    new_node.prev = current.prev
                    current.prev.next = new_node
                    current.prev = new_node
                    self.length += 1
                    break
                index -= 1
                current = current.next
            if index != 0:
                return None
    def pop_back(self):
        if self.tail == None:
            return None
        elif self.tail == self.head:
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        self.length -= 1
    def pop_front(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        self.length -= 1
    def pop(self, index):
        if index == 0:
            self.pop_front()
        elif index == self.length - 1:
            self.pop_back()
        else:
            current = self.head
            while(current != None):
                if index == 0:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    self.length -= 1
                    break
                index -= 1
                current = current.next
            if index != 0:
                return None

    def get_first(self):
        return self.head.value

    def get_last(self):
        return self.tail.value

    def search(self, index):
        if self.head == None or self.tail == None:
            return None
        elif index == 0:
            return self.get_first()
        elif index == self.length - 1:
            return self.get_last()
        current = self.head
        while(current != None):
            if index == 0:
                return current.value
                break
            index -= 1
            current = current.next
        if index != 0:
            return None

    def update(self, index, new_value):
        if self.head == None or self.tail == None:
            return None
        elif index == 0:
            self.head.value = new_value
            return self.get_first()
        elif index == self.length - 1:
            self.tail.value = new_value
            return self.get_last()
        current = self.head
        while(current != None):
            if index == 0:
                current.value = new_value
                return current.value
                break
            index -= 1
            current = current.next
        if index != 0:
            return None

    def __str__(self):
        current = self.head
        res = ''
        while(current != None):
            res += current.value.__str__() + '\n'
            current = current.next
        return res[:-1]