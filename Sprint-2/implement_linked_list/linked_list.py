from __future__ import annotations

from typing import Generic, TypeVar

T = TypeVar("T")


class _Node(Generic[T]):
    """A node in a doubly linked list."""

    __slots__ = ("value", "next", "previous")

    def __init__(self, value: T) -> None:
        self.value = value
        self.next: _Node[T] | None = None
        self.previous: _Node[T] | None = None


class LinkedList(Generic[T]):
    """A doubly linked list supporting O(1) insertion and removal."""

    __slots__ = ("head", "tail")

    def __init__(self) -> None:
        self.head: _Node[T] | None = None
        self.tail: _Node[T] | None = None

    def push_head(self, value: T) -> _Node[T]:
        """Insert value at the head and return its removal handle."""
        node = _Node(value)
        node.next = self.head

        if self.head is None:
            self.tail = node
        else:
            self.head.previous = node

        self.head = node
        return node

    def pop_tail(self) -> T | None:
        """Remove and return the tail value, or None if empty."""
        node = self.tail

        if node is None:
            return None

        value = node.value
        self.remove(node)
        return value

    def remove(self, node: _Node[T]) -> None:
        """Remove a node in O(1) using its handle.

        The node must currently belong to this list.
        """
        if node.previous is None:
            self.head = node.next
        else:
            node.previous.next = node.next

        if node.next is None:
            self.tail = node.previous
        else:
            node.next.previous = node.previous

        # Detach the removed node so it no longer retains list links.
        node.next = None
        node.previous = None
