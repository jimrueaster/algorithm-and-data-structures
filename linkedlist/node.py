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