from core import Array


class UnsortedArray:
    
    def __init__(self, max_size: int, type_code: str = "l"):
        self._array = Array(max_size, type_code)
        self._max_size = max_size
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index: int):
        if index < 0 or index >= self._size:
            raise ValueError("Array index out of range.")
        return self._array[index]
    
    def max_size(self):
        return self._max_size

    def insert(self, value):
        if self._size >= len(self._array):
            raise ValueError("The array is already full")
        self._array[self._size] = value
        self._size += 1
    
    def delete(self, index):
        if self._size == 0:
            raise ValueError("Delete from an empty array")
        elif index < 0 or index >= self._size:
            raise ValueError(f"Index {index} out of range")
        else:
            self._array[index] = self._array[self._size - 1]
            self._size -= 1
    
    def find(self, target: int):
        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        return None
