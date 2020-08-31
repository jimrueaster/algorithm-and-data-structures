#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.node import OneDirectNode


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
    while True:
        print(node.content())
        if None is node.next():
            break
        node = node.next()
