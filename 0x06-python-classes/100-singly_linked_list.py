#!/usr/bin/python3

class Node:
    """Represents a node in a singly linked list
    Attributes:
        __data (int): data stored inside the node
        __next_node (Node): next node in the linked list
    """
    
    def __init__(self, data, next_node=None):
        """Initializes the node
        Args:
            data (int): data stored inside the node
            next_node (Node): next node in the linked list
        Returns:
            None
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """get the data of the node
        Returns:
            data stored inside the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """set the data of the node
        Args:
            value (int): data stored inside the node
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """get the data of next_node
        Returns:
           the next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """set the data of next_node
        Args:
            value (Node): next node in the linked list
        Returns:
            None
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """String representation of Node instance
        Returns:
            Formatted string representing the node
        """
        return str(self.__data)


class SinglyLinkedList:
    """Represents a singly linked list
    Attributes:
        __head (Node): head of the linked list
    """
    def __init__(self):
        """Initializes the linked list
        Returns:
            None
        """
        self.__head = None

    def sorted_insert(self, value):
        """ inserts a new Node instance into the correct sorted position
        Args:
            value (int): data stored inside the new node
        Returns:
            None
        """
        new = Node(value)
        tmp = self.__head
        if tmp is None or tmp.data >= value:
            if tmp:
                new.next_node = tmp
            self.__head = new
            return
        while tmp.next_node is not None:
            if tmp.next_node.data >= value:
                break
            tmp = tmp.next_node
        new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """String representation of SinglyLinkedList instance
        Returns:
            Formatted string representing the linked list
        """
        string = ""
        tmp = self.__head
        while tmp is not None:
            string += str(tmp)
            if tmp.next_node is not None:
                string += "\n"
            tmp = tmp.next_node
        return string