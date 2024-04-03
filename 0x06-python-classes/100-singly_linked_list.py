#!/usr/bin/python3
# Defined by Mugisha David
"""Defines classes of singly-linked list."""

class Node:
    """Represents a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node, optional): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get or set the data of the Node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("Data must be an integer.")
        self.__data = value

    @property
    def next_node(self):
        """Get or set the next_node of the Node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("Next node must be a Node object or None.")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly-linked list."""

    def __init__(self):
        """Initialize a new SinglyLinkedList."""
        self.head = None

    def sorted_insert(self, value):
        """Insert a new Node into the SinglyLinkedList in sorted order.

        Args:
            value (int): The value of the new Node to insert.
        """
        new_node = Node(value)
        if self.head is None or self.head.data > value:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Return a string representation of SinglyLinkedList."""
        values = []
        current = self.head
        while current is not None:
            values.append(str(current.data))
            current = current.next_node
        return '\n'.join(values)
