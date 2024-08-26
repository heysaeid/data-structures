import array


class Array:
    
    def __init__(self, size: int, typecode = "l"):
        self._array = array.array(typecode, [0] * size)
        self._size = size

    def __len__(self):
        return self._size

    def __getitem__(self, index: int):
        if index < 0 or index >= self._size:
            raise ValueError("Array index out of range.")
        return self._array[index]

    def __setitem__(self, index: int, value):
        if index < 0 or index >= self._size:
            raise ValueError("Array assignment index out of range")
        self._array[index] = value

    def __repr__(self):
        return repr(self._array)
