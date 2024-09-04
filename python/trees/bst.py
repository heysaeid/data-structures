"""Binary Search Tree (BST) implementation."""
from __future__ import annotations
from typing import Optional
from stacks.stack import Stack


class BinarySearchTree:

    class Node:

        @staticmethod
        def _node_str(node: type[BinarySearchTree.Node]) -> str:
            return str(node) if node is not None else ''

        def __init__(self, value: any,
                    left: type[BinarySearchTree.Node] = None,
                    right: type[BinarySearchTree.Node] = None) -> None:
            self._value = value
            self._left = left
            self._right = right

        def __str__(self) -> str:
            left_str = BinarySearchTree.Node._node_str(self._left)
            right_str = BinarySearchTree.Node._node_str(self._right)
            return f'{self._value} ({left_str})({right_str})'

        def value(self) -> any:
            return self._value

        def left(self) -> type[BinarySearchTree.Node]:
            return self._left

        def right(self) -> type[BinarySearchTree.Node]:
            return self._right

        def set_left(self, node: type[BinarySearchTree.Node]) -> None:
            self._left = node

        def set_right(self, node: type[BinarySearchTree.Node]) -> None:
            self._right = node

        def find_min_in_subtree(self) -> tuple[type[BinarySearchTree.Node], type[BinarySearchTree.Node]]:
            parent = None
            node = self
            while node.left() is not None:
                parent = node
                node = node.left()
            return node, parent

        def find_max_in_subtree(self) -> tuple[type[BinarySearchTree.Node], type[BinarySearchTree.Node]]:
            parent = None
            node = self
            while node.right() is not None:
                parent = node
                node = node.right()
            return node, parent


    def __init__(self) -> None:
        self._root = None


    def __repr__(self) -> str:
        return f'BinarySearchTree({str(self)})'


    def __str__(self) -> str:
        return BinarySearchTree.Node._node_str(self._root)


    def __len__(self) -> bool:
        stack = Stack()
        stack.push(self._root)
        size = 0
        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                size += 1
                stack.push(node.right())
                stack.push(node.left())
        return size


    def __iter__(self):
        current = self._root
        stack = Stack()
        while current is not None or len(stack) > 0:
            if current is None:
                current = stack.pop()
                yield current.value()
                current = current.right()
            else:
                while current.left() is not None:
                    stack.push(current)
                    current = current.left()
                yield current.value()
                current = current.right()


    def _search(self, value: any) -> tuple[Optional[type[BinarySearchTree.Node]], type[BinarySearchTree.Node]]:
        parent = None
        node = self._root
        while node is not None:
            node_val = node.value()
            if node_val == value:
                return node, parent
            elif value < node_val:
                parent = node
                node = node.left()
            else:
                parent = node
                node = node.right()
        return None, None


    def contains(self, value: any) -> bool:
        return self._search(value)[0] is not None


    def insert(self, value: any) -> None:
        node = self._root
        if node is None:
            self._root = BinarySearchTree.Node(value)
        else:
            while True:
                if value <= node.value():
                    if node.left() is None:
                        node.set_left(BinarySearchTree.Node(value))
                        break
                    else:
                        node = node.left()
                elif node.right() is None:
                    node.set_right(BinarySearchTree.Node(value))
                    break
                else:
                    node = node.right()

    def delete(self, value: any) -> None:
        if self._root is None:
            raise ValueError('Delete on an empty tree')
        node, parent = self._search(value)
        if node is None:
            raise ValueError('Value not found')

        if node.left() is None or node.right() is None:
            maybe_child = node.right() if node.left() is None else node.left()
            if parent is None:
                self._root = maybe_child
            elif value <= parent.value():
                parent.set_left(maybe_child)
            else:
                parent.set_right(maybe_child)
        else:
            max_node, max_node_parent = node.left().find_max_in_subtree()
            if max_node_parent is None:
                new_node = BinarySearchTree.Node(max_node.value(), None, node.right())
            else:
                new_node = BinarySearchTree.Node(max_node.value(), node.left(), node.right())
                max_node_parent.set_right(max_node.left())
            if parent is None:
                self._root = new_node
            elif value <= parent.value():
                parent.set_left(new_node)
            else:
                parent.set_right(new_node)
