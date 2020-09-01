#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.node import *


# ----------------------
#     delete by index
# ----------------------

def delete_by_index(a_head, an_index):
    i = 0
    node = a_head

    while True:
        if i == an_index:
            old_next = node.next()
            if None is old_next:
                raise IndexError('index exceeds.')
            old_next_next = old_next.next()
            node.set_next(old_next_next)

        if None is node.next():
            break

        i += 1
        node = node.next()


head = generate_linked_list()

delete_by_index(head, 0)
delete_by_index(head, 0)

print_one_d_linked_list(head)
