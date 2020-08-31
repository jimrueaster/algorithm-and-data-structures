#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.node import OneDirectNode
from one_direction_linked_list.one_direction_linked_list import print_one_d_linked_list

n0 = OneDirectNode()
n1 = OneDirectNode('aaaa')
n2 = OneDirectNode('bbbb')
n3 = OneDirectNode('cccc')

n0.set_next(n1)
n1.set_next(n2)
n2.set_next(n3)

new = OneDirectNode('new')


def insert_after(head, index, new_node):
    i = 0
    node = head
    while True:
        if i == index:
            old_next = node.next()
            new_node.set_next(old_next)
            node.set_next(new_node)
        if None is node.next():
            break
        i += 1
        node = node.next()


insert_after(n0, 3, new)
print_one_d_linked_list(n0)
