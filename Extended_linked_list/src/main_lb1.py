class Node:
    def __init__(self, node_size):
        self.node_size = node_size
        self.data = list()
        self.next = None
        self.prev = None

    def is_fool(self):
        return len(self.data) == self.node_size

    def __str__(self):
        return ' '.join([str(i) for i in self.data])

    def __del__(self):
        self.data = None
        self.node_size = None
        self.next = None
        self.prev = None
        del self.data
        del self.node_size


class Extended_Linked_List:
    def __init__(self, node_size = 1, auto_balance_flag = True):
        self.__head__ = Node(node_size)
        self.__tail__ = self.__head__
        self.length = 0
        self.node_size = node_size
        self.node_count = 1
        self.auto_balance_flag = auto_balance_flag

    def __sizeof__(self):
        return self.length * int().__sizeof__()

    def fullness(self):
        return f'{self.length / (self.node_count * self.node_size) * 100 :.3f}%'

    def push_back(self, value):
        if not(self.__tail__.is_fool()):
            self.__tail__.data.append(value)
        else:
            self.node_count += 1
            new_node = Node(self.node_size)
            new_node.data += self.__tail__.data[(self.node_size + 1) // 2:]
            self.__tail__.data = self.__tail__.data[:(self.node_size + 1) // 2]
            new_node.data.append(value)
            new_node.prev = self.__tail__
            self.__tail__.next = new_node
            self.__tail__ = new_node
        self.length += 1
        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()

    def push_front(self, value):
        if not(self.__head__.is_fool()):
            self.__head__.data.insert(0, value)
        else:
            self.node_count += 1
            cnt = len(self.__head__.data) - (self.node_size + 1) // 2
            new_node = Node(self.node_size)
            new_node.data.append(value)
            new_node.data += self.__head__.data[:-cnt]
            self.__head__.data = self.__head__.data[-cnt:]
            new_node.next = self.__head__
            self.__head__.prev = new_node
            self.__head__ = new_node
        self.length += 1
        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()

    def insert(self, index, value):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.push_front(value)
        elif index == self.length:
            self.push_back(value)
        else:
            current = self.__head__
            while(current != None and index >= 0):
                if index < len(current.data):
                    if not(current.is_fool()):
                        current.data.insert(index, value)
                    else:
                        current.data.insert(index, value)
                        self.node_count += 1
                        new_node = Node(self.node_size)
                        new_node.data = current.data[(self.node_size + 1) // 2:]
                        current.data = current.data[:(self.node_size + 1) // 2]
                        new_node.prev = current
                        new_node.next = current.next
                        current.next = new_node
                        if current == self.__tail__:
                            self.__tail__ = current
                    self.length += 1
                    break
                index -= len(current.data)
                current = current.next
        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()

    def pop_back(self):
        if self.length != 0:
            self.__tail__.data = self.__tail__.data[:-1]
            self.length -= 1
        if len(self.__tail__.data) == 0 and self.__tail__ != self.__head__:
            self.__tail__.prev.next = None
            tail_node  = self.__tail__
            del self.__tail__
            self.__tail__ = tail_node.prev
            self.node_count -= 1
        else:
            return None

        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()

    def pop_front(self):
        if self.length != 0:
            self.__head__.data = self.__head__.data[1:]
            self.length -= 1
        if len(self.__head__.data) == 0 and self.__head__ != self.__tail__:
            self.__head__.next.prev = None
            head_node = self.__head__
            del self.__head__
            self.__head__ = head_node.next
            self.node_count -= 1
        else:
            return None

        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()
    def pop(self, index):
        if index == None or index < 0 or index >= self.length:
            return None
        elif index == 0:
            self.pop_front()
        elif index == self.length - 1:
            self.pop_back()
        else:
            current = self.__head__
            while (current != None and index >= 0):
                if index < len(current.data):
                    current.data.pop(index)
                    if current != self.__tail__ and len(current.data) < (self.node_size + 1) // 2:
                        length = len(current.data)
                        current.data += current.next.data[:(self.node_size + 1) // 2 - length]
                        current.next.data = current.next.data[(self.node_size + 1) // 2 - length:]
                        if len(current.next.data) < (self.node_size + 1) // 2:
                            current.data += current.next.data
                            next_node = current.next
                            if current.next != self.__tail__:
                                current.next.next.prev = current
                                del current.next
                                current.next = next_node.next
                                self.node_count -= 1
                            else:
                                current.next = None
                                del self.__tail__
                                self.__tail__ = current
                                self.node_count -= 1
                    elif current == self.__tail__:
                        if len(current.data) == 0:
                            if self.__head__ != self.__tail__:
                                self.__tail__.prev.next = None
                                tail_node = self.__tail__
                                del self.__tail__
                                self.__tail__ = tail_node.prev
                                self.node_count -= 1
                            else:
                                return None
                    self.length -= 1
                    break
                index -= len(current.data)
                current = current.next
        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.node_size:
            self.balance()

    def pop_by_value_first(self, value):
        self.pop(self.search_by_value_first(value))

    def pop_by_value_last(self, value):
        self.pop(self.search_by_value_last(value))

    def pop_by_value_all(self, value):
        index = self.search_by_value_first(value)
        while(index != None):
            self.pop(index)
            index = self.search_by_value_first(value)

    def search(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.get_first()
        elif index == self.length - 1:
            return self.get_last()
        current = self.__head__
        while (current != None and index >= 0):
            if index < len(current.data):
                return current.data[index]
            index -= len(current.data)
            current = current.next

    def get_last(self):
        if self.__tail__ != None and len(self.__tail__.data) != 0:
            return self.__tail__.data[-1]

    def get_first(self):
        if self.__head__ != None and len(self.__head__.data) != 0:
            return self.__head__.data[0]
    def search_by_value_first(self, value):
        current = self.__head__
        index = 0
        while (current != None):
            for i in range(len(current.data)):
                if current.data[i] == value:
                    return i + index
            index += len(current.data)
            current = current.next
        return None

    def search_by_value_last(self, value):
        current = self.__head__
        index = 0
        res = -1
        while (current != None):
            for i in range(len(current.data)):
                if current.data[i] == value:
                    res = i + index
            index += len(current.data)
            current = current.next
        if res != -1:
            return res
        return None

    def search_by_value_all(self, value):
        current = self.__head__
        indexes = list()
        index = 0
        while (current != None):
            for i in range(len(current.data)):
                if current.data[i] == value:
                    indexes.append(i + index)
            index += len(current.data)
            current = current.next
        if len(indexes) != 0:
            return indexes
        return None

    def replication_by_func(self, func, buffer):
        current = self.__head__
        while(current != None):
            flag = True
            for i in range(len(current.data)):
                if not(func(current.data[i])):
                    flag = False
                    break
            if flag:
                buffer.append((current,current.__str__()))
            current = current.next

    def replication_by_index(self, index, buffer):
        current = self.__head__
        while(current != None):
            if index < len(current.data):
                buffer.append((current,current.__str__()))
                break
            index -= len(current.data)
            current = current.next

    def filter(self, func):
        current = self.__head__
        index = 0
        values = list()
        while(current != None):
            for i in range(len(current.data)):
                if not(func(current.data[i])):
                    values.append(current.data[i])
            index += len(current.data)
            current = current.next
        if len(values) != 0:
            for i in values:
                self.pop_by_value_first(i)

    def calculate_optimal_node_size(self):
        return int(self.length ** 0.5)

    def balance(self, node_size = None):
        if node_size == None:
            node_size = self.calculate_optimal_node_size()
        if node_size >= self.length:
            self.node_size = node_size
            self.node_count = 1
            self.__head__.node_size = node_size
            if self.__head__ != self.__tail__:
                current = self.__head__.next
                while(current != None):
                    self.__head__.data += current.data
                    current_copy = current.next
                    if current != self.__tail__:
                        current.prev.next = current.next
                        current.next.prev = current.prev

                    else:
                        current.prev.next = None
                    del current
                    current = current_copy
                self.__tail__ = self.__head__
        elif node_size > self.node_size:
            current = self.__head__
            self.node_size = node_size
            while(current != self.__tail__ and current != None):
                current.node_size = node_size
                temp = current.next
                while(temp != None):
                    cnt = (node_size + 1) // 2 - len(current.data)
                    if len(temp.data) > cnt:
                        current.data += temp.data[:cnt]
                        temp.data = temp.data[cnt:]
                        break
                    else:
                        self.node_count -= 1
                        current.data += temp.data
                        if temp != self.__tail__:
                            temp.prev.next = temp.next
                            temp.next.prev = temp.prev
                        else:
                            self.__tail__.prev.next = None
                            tail_copy = self.__tail__
                            del self.__tail__
                            self.__tail__ = tail_copy.prev
                            del tail_copy
                        temp = temp.next
                current = current.next
        elif node_size < self.node_size:
            current = self.__head__
            self.node_size = node_size
            while(current != self.__tail__):
                current.node_size = node_size
                if len(current.data) > (node_size + 1) // 2:
                    cnt = len(current.data) - (node_size + 1) // 2
                    current.next.data = current.data[-cnt:] + current.next.data
                    current.data = current.data[:-cnt]
                current = current.next
            while(len(self.__tail__.data) > (node_size + 1) // 2):
                new_node = Node(node_size)
                cnt = len(self.__tail__.data) - (node_size + 1) // 2
                new_node.data = self.__tail__.data[-cnt:]
                self.__tail__.data = self.__tail__.data[:-cnt]
                new_node.prev = self.__tail__
                self.__tail__.next = new_node
                self.__tail__ = new_node
                self.node_count += 1

    def __iadd__(self, other):
        self.__make_beaty__()
        other.__make_beaty__()
        other.__head__.prev = self.__tail__
        self.__tail__.next = other.__head__
        self.__tail__ = other.__tail__
        self.length += other.length
        self.node_count += other.node_count
        if self.auto_balance_flag and self.calculate_optimal_node_size() != self.length:
            self.balance()
        return self

    def __copy__(self):
        extended_linked_list_copy = Extended_Linked_List(self.node_size)
        extended_linked_list_copy.length = self.length
        extended_linked_list_copy.__tail__ = self.__tail__
        extended_linked_list_copy.__head__ = self.__head__
        extended_linked_list_copy.node_count = self.node_count
        return extended_linked_list_copy

    def __deepcopy__(self):
        extended_linked_list_deep_copy = Extended_Linked_List(self.node_size)
        extended_linked_list_deep_copy.length = self.length
        extended_linked_list_deep_copy.node_count = self.node_count
        current = self.__head__
        while(current != None):
            extended_linked_list_deep_copy.__tail__.data = [i for i in current.data]
            if current.next != None:
                new_node = Node(self.node_size)
                new_node.prev = extended_linked_list_deep_copy.__tail__
                extended_linked_list_deep_copy.__tail__.next = new_node
                extended_linked_list_deep_copy.__tail__ = new_node
            current = current.next
        return extended_linked_list_deep_copy

    def __del__(self):
        current = self.__head__
        while(current != None):
            temp = current.next
            current.__del__()
            current = temp
        self.length = 0

    def __make_beaty__(self):
        if len(self.__tail__.data) > ((self.node_size + 1) // 2) :
            cnt = len(self.__tail__.data) - ((self.node_size + 1) // 2)
            new_node = Node(self.node_size)
            new_node.data = self.__tail__.data[-cnt:]
            self.__tail__.data = self.__tail__.data[:-cnt]
            new_node.prev = self.__tail__
            self.__tail__.next = new_node
            self.__tail__ = new_node
        if len(self.__head__.data) > ((self.node_size + 1) // 2) :
            cnt = len(self.__head__.data) - ((self.node_size + 1) // 2)
            new_node = Node(self.node_size)
            new_node.data = self.__head__.data[:cnt]
            self.__head__.data = self.__head__.data[cnt:]
            new_node.next = self.__head__
            self.__head__.prev = new_node
            self.__head__ = new_node

    def __str__(self):
        if self.length == 0:
            return 'Empty'
        res = ''
        self.__make_beaty__()
        index = 0
        current = self.__head__
        while(current != None):
            res += f'Node {index}: ' + current.__str__() + '\n'
            current = current.next
            index += 1
        return res[:-1]


def calculate_optimal_node_size(num_elements):
    return((num_elements * 4 + 63) // 64 + 1)

if __name__ == "__main__":
    data = list(map(int, input().split()))
    ell = Extended_Linked_List(auto_balance_flag=False)

    ell.balance(calculate_optimal_node_size(len(data)) * 2)

    for i in data:
        ell.push_back(i)

    print(ell)