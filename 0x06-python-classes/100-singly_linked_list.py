#!/usr/bin/python3
"""
This module defines a singly linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) != int:
            raise TypeError('data must be an integer')

        self._data = value

    @property
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError('next_node must a Node object')
        self.__next_node = value


class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        if self.__head is None:
            self.__head = Node(value)
        else:
            current = self.__head
            previous = None
            while current and vakue > current.data:
                previous = current
                current = current.next_node
            if current is None:
                previous.next_node = Node(value)
            elif current is self.__head and previous is None:
                self.__head = Node(value, current)
            else:
                newNode = Node(value, current)
                previous.next_node = newNode

    def __repr__(self):
        node = self.__head
        txt = ''
        while 1:
            txt += str(node.data)
            node = node.next_node
            if node.next_node is None:
                break
            else:
                txt += '\n'
        return txt
