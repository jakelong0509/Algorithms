import numpy as np
import os
import sys
from Queue import Queue
from node import Node

class Heap:
    def __init__(self):
        self.root = None
        self.i = 0
        self.nodes = []

    def constructHeap(self, arr = []):
        if arr == []:
            return

        node = Node(arr[0])
        self.root = node
        self.nodes.append(node)
        for value in arr[1:]:
            n = self.nodes[self.i]
            node = Node(value)
            node.parent = n
            self.nodes.append(node)
            if n.left == None:
                n.left = node
            else:
                n.right = node
                self.i += 1


            while node.parent != None and node.parent.value > node.value:
                node.swap()
                node = node.parent

    def addValue(self, value):
        node = Node(value)
        if self.root == None:
            self.nodes.append(node)
            self.root = node
            return

        n = self.nodes[self.i]
        node.parent = n
        self.nodes.append(node)
        if n.left == None:
            n.left = node
        else:
            n.right = node
            self.i += 1

        while node.parent != None and node.parent.value > node.value:
            node.swap()
            node = node.parent
