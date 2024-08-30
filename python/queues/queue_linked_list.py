from typing import Any
from linked_lists.doubly_linked_list import DoublyLinkedList 


class QueueLinkedList:
    def __init__(self):
        self._data = DoublyLinkedList()


    def __len__(self):
        return len(self._data)


    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()


    def __str__(self):
        return str(self._data)


    def __repr__(self):
        return f'Queue({str(self._data)})'


    def is_empty(self) -> bool:
        return self._data.is_empty()


    def enqueue(self, value: Any) -> None:
        self._data.insert_to_back(value)


    def dequeue(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self._data.delete_from_front()