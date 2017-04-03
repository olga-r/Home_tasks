class Node(object):
    __slots__ = ['data','next_node']
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node
    def set_next(self, new_next):
        self.next_node = new_next
    def set_data(self, new_data):
        self.data = new_data

class LinkedList(object):
    __slots__ = ['head', '__current', '__length', '__i']
    def __init__(self, data = None):
        first_node = Node(data)
        self.head = first_node
        self.__current = self.head
        if self.head.data is None:
             self.__length = 0
        else:
             self.__length = 1
    
    def __iter__(self):
        self.__current = self.head
        return self
        
    def __next__(self):
        if (self.__current is None) or len(self) == 0:
            raise StopIteration
        self.__i = self.__current
        self.__current = self.__current.next_node
        return self.__i
    
    def __len__(self):
        return self.__length
    
    def __getitem__(self, index):
        if index >= len(self):
            raise IndexError('LinkedList index out of range')
        iter(self)
        for i in range(index+1):
            result = next(self)        
        return result
    
    def __setitem__(self, index, data):
        if index >= len(self):
            raise IndexError('LinkedList assignment index out of range')
        if index < len(self):
            self[index].set_data(data)
    
    def insert(self, index, data):
        if index == len(self):
            node = Node(data)
            self[index-1].set_next(node)
        elif index < len(self) and index > 0:
            node = Node(data, self[index])
            self[index-1].set_next(node)
        elif index == 0:
            node = Node(data, self[index])
            self.head = node
            self.__current = self.head
        self.__length += 1

    def append(self, data):
        if self.__length == 0:
            self.head.set_data(data) 
        else:
            node = Node(data)
            self[len(self)-1].set_next(node)
            self.__current = self.head
        self.__length += 1
    
    def __contains__(self, data):
        for i in self:
            if i.data == data:
                return True
        return False
        
    def __add__(self, other):
        L = LinkedList()
        for i in self:
            L.append(i.data)
        for i in other:
            L.append(i.data)
        return L
        


