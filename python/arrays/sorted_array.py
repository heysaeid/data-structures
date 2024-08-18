from core import Array


class SortedArray:
    
    def __init__(self, max_size: int, type_code: str = "l"):
        self._array = Array(max_size, type_code)
        self._max_size = max_size
        self._size = 0

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or index >= self._size:
            raise ValueError("Array index out of range")
        return self._array[index]

    def insert(self, value):
        if self._size >= self._max_size:
            raise ValueError("The array is already full")
        for index in range(self._size, 0, -1):
            if self._array[index - 1] <= value:
                self._array[self._size] = value
                self._size += 1
                return
            else:
                self._array[index] = self._array[index - 1]
        self._array[0] = value
        self._size += 1
    
    def binary_search(self, target: int):
        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_value = self._array[mid_index]
            if mid_value == target:
                return mid_index
            elif mid_value > target:
                right = mid_index - 1
            else:
                left = mid_index + 1
        return None

    def delete(self, target):
        index = self.binary_search(target)
        for index in range(index, self._size - 1):
            self._array[index] = self._array[index + 1]
        self._size -= 1