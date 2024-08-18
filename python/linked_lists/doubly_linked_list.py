class DoublyLinkedList:
    
    def __init__(self):
        self._head = None
        self._tail= None

    class Node:
        
        def __init__(self, data):
            self._data = data
            self._next = None
            self._prev = None
        
        def data(self):
            return self._data
        
        def next(self):
            return self._next
        
        def has_next(self):
            return self._next is not None
        
        def append(self, next_node):
            self._next = next_node
            if next_node is not None:
                next_node._prev = self
        
        def prev(self):
            return self._prev
        
        def has_prev(self):
            return self._prev is not None
        
        def prepend(self, prev_node):
            self._prev = prev_node
            if prev_node is not None:
                prev_node.next = self

    def insert_in_front(self, data):
        if self._head is None:
            self._head = self._tail = DoublyLinkedList.Node(data)
        else:
            old_head = self._head
            self._head = DoublyLinkedList.Node(data)
            self._head.append(old_head)

    def insert_in_end(self, data):
        if self._tail is None:
            self._head = self._tail = DoublyLinkedList.Node(data)
        else:
            old_tail = self._tail
            self._tail = DoublyLinkedList.Node(data)
            self._tail.prepend(old_tail)

    def _search(self, target):
        current = self._head
        while current.has_next():
            if current.data() == target:
                return current
            current = current.next()
        return None

    def delete(self, target):
        node = self._search(target)
        if node is None:
            raise ValueError(f"Target {target} not found in the list")
        if node.prev() is None:
            self._head = node.next()
            if self._head is None:
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            self._tail = node.prev()
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            del node
