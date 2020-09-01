#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.util import *


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


head = generate_linked_list()

new = OneDirectNode('new')
insert_after(head, 1, new)

print_one_d_linked_list(head)
