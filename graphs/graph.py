from __future__ import annotations
from typing import Any, Type, Tuple
from linked_lists.singly_linked_list import SinglyLinkedList
from queues.queue import Queue
from stacks.stack import Stack

class Graph:

    class Vertex:

        def __init__(self, key: Any):
            self.id = key
            self._adj_list = SinglyLinkedList()

        def __eq__(self, other: Type[Graph.Vertex]):
            return self.id == other.id

        def __hash__(self) -> int:
            return hash(repr(self))

        def __repr__(self) -> str:
            return f'Vertex({repr(self.id)})'

        def __str__(self) -> str:
            return f'<{str(self.id)}>'

        def has_edge_to(self, destination_vertex: Type[Graph.Vertex]) -> bool:
            return self._adj_list.search(lambda v: v == destination_vertex) is not None

        def add_edge_to(self, destination_vertex: Type[Graph.Vertex]) -> None:
            if self.has_edge_to(destination_vertex):
                raise ValueError(f'Edge already exists: {self} -> {destination_vertex}')
            self._adj_list.insert_in_front(destination_vertex)

        def delete_edge_to(self, destination_vertex: Type[Graph.Vertex]):
            try:
                self._adj_list.delete(destination_vertex)
            except ValueError as e:
                raise ValueError(f'Edge does not exist: {self} -> {destination_vertex}') from e

        def outgoing_edges(self) -> list[Tuple[Any, Any]]:
            return [(self.id, v.id) for v in self._adj_list]


    def __init__(self):
        self._adj = {}


    def __repr__(self) -> str:
        def edges_repr(edges):
            return f"[{', '.join((f'->{u}' for (_, u) in edges))}]"

        adj_lst_repr = (f'{repr(v)}: {edges_repr(v.outgoing_edges())}' for v in self._adj.values())
        return f'Graph({" | ".join(adj_lst_repr)})'


    def _get_vertex(self, key: Any) -> Type[Graph.Vertex]:
        if key not in self._adj:
            raise ValueError(f'Vertex {key} does not exist!')
        return self._adj[key]


    def insert_vertex(self, key: Any) -> None:
        if key in self._adj:
            raise ValueError(f'Vertex {key} already exists!')
        self._adj[key] = Graph.Vertex(key)


    def has_vertex(self, key: Any) -> bool:
        return key in self._adj


    def delete_vertex(self, key: Any) -> None:
        v = self._get_vertex(key)
        for u in self._adj.values():
            if u != v and u.has_edge_to(v):
                u.delete_edge_to(v)
        del self._adj[key]


    def get_vertices(self) -> set[Any]:
        return set(self._adj.keys())


    def vertex_count(self) -> int:
        return len(self._adj)


    def insert_edge(self, key1: Any, key2: Any) -> None:
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.add_edge_to(v2)


    def has_edge(self, key1: Any, key2: Any) -> bool:
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        return v1.has_edge_to(v2)


    def delete_edge(self, key1: Any, key2: Any) -> None:
        v1 = self._get_vertex(key1)
        v2 = self._get_vertex(key2)
        v1.delete_edge_to(v2)


    def get_edges(self) -> set[tuple[Any, Any]]:
        return set(e for v in self._adj.values() for e in v.outgoing_edges())


    def edge_count(self) -> int:
        return sum(len(v.outgoing_edges()) for v in self._adj.values())


    def bfs(self, start_vertex: Any, target_vertex: Any) -> list[Any]:
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if not self.has_vertex(target_vertex):
            raise ValueError(f'Target vertex {target_vertex} does not exist!')

        def reconstruct_path(pred: dict[Any, Any], target: Any) -> list[Any]:
            path = []
            while target:
                path.append(target)
                target = pred[target]
            return path[::-1]

        distance = {v: float('inf') for v in self._adj}
        predecessor = {v: None for v in self._adj}

        queue = Queue(self.vertex_count())
        queue.enqueue(start_vertex)
        distance[start_vertex] = 0

        while not queue.is_empty():
            u = queue.dequeue()
            if u == target_vertex:
                return reconstruct_path(predecessor, target_vertex)

            for (_, v) in self._get_vertex(u).outgoing_edges():
                if distance[v] == float('inf'):
                    distance[v] = distance[u] + 1
                    predecessor[v] = u
                    queue.enqueue(v)

        return None

    def dfs(self, start_vertex: Any, color: dict[Any, str] = None) -> Tuple[bool, dict[Any, str]]:
        if not self.has_vertex(start_vertex):
            raise ValueError(f'Start vertex {start_vertex} does not exist!')
        if color is None:
            color = {v: 'white' for v in self._adj}
        acyclic = True
        stack = Stack()
        stack.push((False, start_vertex))
        while not stack.is_empty():
            (mark_as_black, v) = stack.pop()
            col = color.get(v, 'white')
            if mark_as_black:
                color[v] = 'black'
            elif col == 'grey':
                acyclic = False
            elif col == 'white':
                color[v] = 'grey'
                stack.push((True, v))
                for (_, w) in self._get_vertex(v).outgoing_edges():
                    stack.push((False, w))
        return acyclic, color