import numpy as np
import os
import sys
from Queue import Queue
from node import node

class Heap:
    def __init__(self):
        self.root = None

    def constructHeap(self, arr):
        queue = Queue()
        n = Node(arr[0])
        for value in arr[1:]:
            node = Node(value)
            queue.enqueue(value)
            if n.left != None:
                n.left = node
            else:
                n.right = node
            while node.parent.value != None and node.parent.value > node.value:
                node.swap()
                node = node.parent
