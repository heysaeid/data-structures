class SinglyLinkedList:
    
    def __init__(self):
        self._head = None

    class Node:

        def __init__(self, data, next_node = None):
            self._data = data
            self._next_node = next_node
        
        def data(self):
            return self._data
        
        def next(self):
            return self._next_node
        
        def has_next(self):
            return self._next_node is not None
        
        def append(self, next_node):
            self._next_node = next_node

    def insert(self, data):
        current = self._head
        if current is None:
            self._head = SinglyLinkedList.Node(data)
        else:
            while current.has_next():
                current = current.next()
            current.append(SinglyLinkedList.Node(data))

    def insert_in_front(self, data):
        old_head = self._head
        self._head = SinglyLinkedList.Node(data, old_head)

    def _search(self, target):
        current = self._head
        while current.has_next():
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        current = self._head
        previous = None
        while current.has_next():
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
