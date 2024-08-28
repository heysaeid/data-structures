from typing import Any


class Queue:

    def __init__(self, max_size):
        if max_size <= 1:
            raise ValueError(f'Invalid size (a queue must have at least two elements): {max_size}')
        self._data = [None] * max_size
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0


    def __len__(self):
        return self._size


    def __iter__(self):
        while not self.is_empty():
            yield self.dequeue()


    def __str__(self):
        def iterate():
            if self.is_empty():
                return
            front = self._front
            if front > self._rear:
                while front < self._max_size:
                    yield self._data[front]
                    front += 1
                front = 0
            while front < self._rear:
                yield self._data[front]
                front += 1

        return str([x for x in iterate()])


    def __repr__(self):
        return f'Queue({str(self)})'


    def is_empty(self) -> bool:
        return len(self) == 0



    def is_full(self) -> bool:
        return len(self) == self._max_size


    def enqueue(self, value: Any) -> None:
        if self.is_full():
            raise ValueError('The queue is already full!')
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1


    def dequeue(self) -> Any:
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")

        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return value