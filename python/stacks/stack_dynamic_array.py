import copy
from typing import Any


class Stack:
    def __init__(self) -> None:
        self._data = []


    def __len__(self):
        return len(self._data)


    def __iter__(self):
        while not self.is_empty():
            yield self.pop()


    def __str__(self):
        return str(self._data[::-1])


    def __repr__(self):
        return f'Stack({str(self._data[::-1])})'


    def is_empty(self) -> bool:
        return len(self._data) == 0


    def push(self, value: Any) -> None:
        self._data.append(value)


    def pop(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self._data.pop()


    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        return copy.deepcopy(self._data[-1])
