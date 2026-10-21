
from typing import Generic, TypeVar


K = TypeVar("K")
V = TypeVar("V")


class _Node(Generic[K, V]):
    """A node storing a cache key, value, and linked-list pointers."""

    __slots__ = ("key", "value", "previous", "next")

    def __init__(self, key: K, value: V) -> None:
        self.key = key
        self.value = value
        self.previous: _Node[K, V] | None = None
        self.next: _Node[K, V] | None = None


class LruCache(Generic[K, V]):
    """
    Least Recently Used (LRU) cache.

    Most recently used entries are at the head.
    Least recently used entries are at the tail.

    Dictionary: key -> node
    Doubly linked list: usage order

    get() and set() have O(1) expected time complexity.
    """

    def __init__(self, limit: int) -> None:
        if limit <= 0:
            raise ValueError("Cache limit must be greater than zero")

        self.limit = limit
        self.cache: dict[K, _Node[K, V]] = {}
        self.head: _Node[K, V] | None = None
        self.tail: _Node[K, V] | None = None

    def _remove(self, node: _Node[K, V]) -> None:
        """Remove an existing node from the linked list in O(1)."""

        if node.previous is not None:
            node.previous.next = node.next
        else:
            self.head = node.next

        if node.next is not None:
            node.next.previous = node.previous
        else:
            self.tail = node.previous

        node.previous = None
        node.next = None

    def _add_to_head(self, node: _Node[K, V]) -> None:
        """Insert a detached node at the most-recently-used end."""

        node.previous = None
        node.next = self.head

        if self.head is not None:
            self.head.previous = node
        else:
            self.tail = node

        self.head = node

    def _move_to_head(self, node: _Node[K, V]) -> None:
        """Mark an existing entry as most recently used."""

        if node is self.head:
            return

        self._remove(node)
        self._add_to_head(node)

    def get(self, key: K) -> V | None:
        """Return a value and mark its entry as recently used."""

        node = self.cache.get(key)

        if node is None:
            return None

        self._move_to_head(node)
        return node.value

    def set(self, key: K, value: V) -> None:
        """Insert or update an entry, evicting the LRU entry if needed."""

        node = self.cache.get(key)

        if node is not None:
            # Updating an entry also counts as use.
            node.value = value
            self._move_to_head(node)
            return

        # Evict before inserting to keep the capacity bounded.
        if len(self.cache) >= self.limit:
            lru_node = self.tail
            assert lru_node is not None

            self._remove(lru_node)
            del self.cache[lru_node.key]

        new_node = _Node(key, value)
        self._add_to_head(new_node)
        self.cache[key] = new_node

    def __len__(self) -> int:
        """Return the number of entries currently stored."""

        return len(self.cache)
