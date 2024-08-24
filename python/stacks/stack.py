import copy
from typing import Any
from linked_lists.singly_linked_list import SinglyLinkedList


class Stack:

    def __init__(self) -> None:
        self._data = SinglyLinkedList()


    def __len__(self):
        return len(self._data)



    def __iter__(self):
        while not self.is_empty():
            yield self.pop()


    def __str__(self):
        return str(self._data)


    def __repr__(self):
        return f'Stack({str(self._data)})'


    def is_empty(self) -> bool:
        return self._data.is_empty()


    def push(self, value: Any) -> None:
        self._data.insert_in_front(value)


    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self._data.delete_from_front()


    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        return copy.deepcopy(self._data._head.data())
