from math import floor, sqrt
from decimal import Decimal
from typing import Any, Callable
from linked_lists.singly_linked_list import SinglyLinkedList


class HashTable:
    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, buckets: int, extract_key:  Callable[..., Any]=hash) -> None:
        if buckets <= 0:
            raise ValueError(f'Invalid size for the hash table (must be positive): {buckets}')
        self._m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key = extract_key


    def __len__(self):
        return sum((len(bucket) for bucket in self._data))


    def _hash(self, key: int):
        return floor(abs(self._m * ((Decimal(key) * HashTable.__A__) % 1)))


    def is_empty(self) -> int:
        return len(self) == 0


    def search(self, key: int) -> Any:
        index = self._hash(key)
        value_matches_key = lambda v: self._extract_key(v) == key
        return self._data[index].search(value_matches_key)


    def insert(self, value: Any) -> None:
        index = self._hash(self._extract_key(value))
        self._data[index].insert_in_front(value)


    def contains(self, value: Any) -> bool:
        return self.search(self._extract_key(value)) is not None


    def delete(self, value: Any) -> None:
        index = self._hash(self._extract_key(value))
        try: 
            self._data[index].delete(value)
        except ValueError as exc:
            raise ValueError(f'No element with value {value} was found in the hash table.') from exc