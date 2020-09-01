#!/usr/bin/python3
# -*- coding:utf-8 -*-


from one_direction_linked_list.node import *

# todo improve this 
# ----------------------
#     delete by value
# ----------------------

def delete_by_value(a_head, a_value):
    node = a_head

    while True:
        if None is node.next():
            break

        if node.next().content() == a_value:
            old_next = node.next()
            if None is old_next:
                raise ValueError('value not exists.')
            old_next_next = old_next.next()
            node.set_next(old_next_next)

        if None is node.next():
            break

        node = node.next()


head = generate_linked_list()

delete_by_value(head, 'cccc')

print_one_d_linked_list(head)
