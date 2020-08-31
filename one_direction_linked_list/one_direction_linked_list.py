#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.node import OneDirectNode

n1 = OneDirectNode('aaaa')
n2 = OneDirectNode('bbbb')
n3 = OneDirectNode('cccc')

n1.set_next(n2)
n2.set_next(n3)


def print_one_d_linked_list(head):
    node = head
    while True:
        print(node.content())
        if None is node.next():
            break
        node = node.next()


print_one_d_linked_list(n1)
