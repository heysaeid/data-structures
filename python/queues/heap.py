from typing import Any, List, Optional


class Heap:

    def __init__(self, elements: List[Any] = None, element_priority = lambda x: x) -> None:
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []


    def __len__(self) -> int:
        return len(self._elements)


    def _has_lower_priority(self, element_1: Any, element_2: Any) -> bool:
        return self._priority(element_1) < self._priority(element_2)


    def _has_higher_priority(self, element_1: Any, element_2: Any) -> bool:
        return self._priority(element_1) > self._priority(element_2)


    def _validate(self) -> bool:
        current_index = 0
        first_leaf = self._first_leaf_index()
        while current_index < first_leaf:
            current_element: float = self._elements[current_index]
            first_child = self._left_child_index(current_index)
            last_child_guard = min(first_child + 2, len(self))
            for child_index in range(first_child, last_child_guard):
                if self._has_lower_priority(current_element,  self._elements[child_index]):
                    return False
            current_index += 1
        return True


    def _left_child_index(self, index) -> int:
        return index * 2 + 1


    def _parent_index(self, index: int) -> int:
        return (index - 1) // 2


    def _highest_priority_child_index(self, index: int) -> Optional[int]:
        first_index = self._left_child_index(index)

        if first_index >= len(self):
            return None

        if first_index + 1 >= len(self):
            return first_index

        if self._has_higher_priority(self._elements[first_index], self._elements[first_index + 1]):
            return first_index
        else:
            return first_index + 1


    def _first_leaf_index(self):
        return len(self) // 2


    def _push_down(self, index: int) -> None:
        assert 0 <= index < len(self._elements)
        element = self._elements[index]
        current_index = index
        while True:
            child_index = self._highest_priority_child_index(current_index)
            if child_index is None:
                break
            if self._has_lower_priority(element, self._elements[child_index]):
                self._elements[current_index] = self._elements[child_index]
                current_index = child_index
            else:
                break

        self._elements[current_index] = element


    def _bubble_up(self, index: int) -> None:
        assert 0 <= index < len(self._elements)
        element = self._elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self._elements[parent_index]
            if self._has_higher_priority(element, parent):
                self._elements[index] = parent
                index = parent_index
            else:
                break

        self._elements[index] = element


    def _heapify(self, elements: List[Any]) -> None:
        self._elements = elements[:]
        last_inner_node_index = self._first_leaf_index() - 1
        for index in range(last_inner_node_index, -1, -1):
            self._push_down(index)


    def is_empty(self) -> bool:
        return len(self) == 0


    def top(self) -> Any:
        if self.is_empty():
            raise ValueError('Method top called on an empty heap.')
        if len(self) == 1:
            element = self._elements.pop()
        else:
            element = self._elements[0]
            self._elements[0] = self._elements.pop()
            self._push_down(0)

        return element


    def peek(self) -> Any:
        if self.is_empty():
            raise ValueError('Method peek called on an empty heap.')
        return self._elements[0]


    def insert(self, element: Any) -> None:
        self._elements.append(element)
        self._bubble_up(len(self._elements) - 1)