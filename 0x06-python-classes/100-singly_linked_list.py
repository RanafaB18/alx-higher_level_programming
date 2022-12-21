#!/usr/bin/python3
"""Define a linked list and Node"""


class Node:
    """Defines a node"""

    def __init__(self, data, next_node=None) -> None:
        """Setup node

        Args:
            self: object
            data: value of node
            next_node: pointer to next node

        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data getter function

        Args:
            self: object

        Returns:
            data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """data setter function

        Args:
            self: object
            value: new value

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """next_node getter function

        Args:
            self: object

        Returns:
            next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """next_node setter function

        Args:
            self: object
            value: new value

        Returns:
            None
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Define a Singly Linked List"""

    def __init__(self) -> None:
        """Setup linked list

        Args:
            self: object

        Returns:
            None
        """
        self.__head = None

    def __str__(self) -> str:
        """Generate linked list

        Args:
            self: object
        """
        output = ""
        temp = self.__head
        while temp:
            output += str(temp.data) + "\n"
            temp = temp.next_node
        return output[:-1]

    def sorted_insert(self, value):
        """Insert while sorting

        Args:
            self: object
            value: inserted node's value

        Returns:
            None
        """
        node = Node(value)
        if not self.__head:
            self.__head = node
            return
        if value < self.__head.data:
            node.next_node = self.__head
            self.__head = node
            return
        temp = self.__head
        while (temp.next_node and temp.next_node.data < value):
            temp = temp.next_node
        if temp.next_node:
            node.next_node = temp.next_node
        temp.next_node = node
