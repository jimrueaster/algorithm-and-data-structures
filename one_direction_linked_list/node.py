#!/usr/bin/python3
# -*- coding:utf-8 -*-


class OneDirectNode:

    def __init__(self, a_content=None, a_next=None):
        self.__content = a_content
        self.__next = a_next

    def content(self):
        return self.__content

    def set_next(self, a_next_node):
        self.__next = a_next_node

    def next(self):
        return self.__next


def generate_linked_list():
    """
    :return head node
    """
    result = OneDirectNode()
    n1 = OneDirectNode('aaaa')
    n2 = OneDirectNode('bbbb')
    n3 = OneDirectNode('cccc')

    result.set_next(n1)
    n1.set_next(n2)
    n2.set_next(n3)

    return result


def print_one_d_linked_list(head):
    node = head.next()
    while node:
        print(node.content())
        if None is node.next():
            break
        node = node.next()
