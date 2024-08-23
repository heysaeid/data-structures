import arrays.core as core
from typing import Union


class DynamicArray:

    def __init__(self, initial_capacity: int = 1, type_code: str = 'l') -> None:
        self._array = core.Array(initial_capacity, type_code)
        self._capacity = initial_capacity
        self._size = 0
        self._type_code = type_code


    def __len__(self) -> int:
        return self._size


    def __getitem__(self, index) -> Union[int, float]:
        if index >= self._size:
            raise IndexError(f'Index out of bound: {index}')
        return self._array[index]


    def __repr__(self) -> str:
        return repr(self._array._array[:self._size])    


    def __iter__(self):
        for i in range(self._size):
            yield self._array[i]


    def _is_full(self):
        return self._size >= self._capacity
    
    
    def _double_size(self):
        assert(self._capacity  == self._size)
        old_array = self._array
        self._array = core.Array(self._capacity * 2, self._type_code)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

        assert(self._array._size == self._capacity)


    def _halve_size(self):
        old_array = self._array
        self._array = core.Array(self._capacity // 2, self._type_code)
        self._capacity //= 2
        for i in range(self._size):
            self._array[i] = old_array[i]


    def is_empty(self):
        return len(self) == 0


    def insert(self, value: Union[int, float]) -> None:
        if self._is_full():
            self._double_size()

        self._array[self._size] = value
        self._size += 1


    def find(self, target: Union[int, float]) -> Union[int, None]:
        for i in range(self._size):
            if self._array[i] == target:
                return i
        return None


    def delete(self, target: Union[int, float]) -> None:
        index = self.find(target)
        if index is None:
            raise ValueError(f'Unable to delete element {target}: the entry is not in the array')

        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1    

        if self._capacity > 1 and self._size <= self._capacity/4:
            self._halve_size()