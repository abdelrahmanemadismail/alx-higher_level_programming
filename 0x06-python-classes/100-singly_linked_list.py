#!/usr/bin/python3
"""
This module defines a singly linked list and its associated methods.

Classes:
    - Node: Represents a node of a singly linked list.
    - SinglyLinkedList: Represents a singly linked list.
"""


class Node:
    """
    Represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node instance.

        Args:
            data (int): The data stored in the node.
            next_node (Node, optional): next node of sll (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data attribute.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data attribute.

        Args:
            value (int): The data stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next_node attribute.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next_node attribute.

        Args:
            value (Node): The next node in the linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes a new SinglyLinkedList instance with an empty list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position (increasing order)

        Args:
            value (int): The value to be inserted into the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while (
                    current.next_node is not None and
                    current.next_node.data <= value
            ):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result[:-1]
