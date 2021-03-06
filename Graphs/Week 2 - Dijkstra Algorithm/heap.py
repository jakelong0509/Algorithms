import numpy as np
import os
import sys
from Queue import Queue
from node import Node

class Heap:
    def __init__(self):
        self.root = None
        self.nodes = [Node(0)]

    def constructHeap(self, arr = []):
        if arr == []:
            return

        node = Node(arr[0])
        self.root = node
        self.nodes.append(node)
        i = 2
        for value in arr[1:]:
            new_node = Node(value)
            self.nodes.append(new_node)
            self.swap_with_parent(i)
            i += 1

    def parent(self, i):
        return self.nodes[int(np.floor(i/2))]


    def swap_with_parent(self, child_index):
        while self.nodes[int(np.floor(child_index/2))].value > self.nodes[child_index].value:
            parent_index = int(np.floor(child_index/2))
            self.swap_two_nodes(parent_index, child_index)
            child_index = parent_index
            if child_index == 1:
                break

    def swap_two_nodes(self, parent_index, child_index):
        temp_node = self.nodes[parent_index]
        self.nodes[parent_index] = self.nodes[child_index]
        self.nodes[child_index] = temp_node

    def swap_with_childrens(self, parent_index):
        while True:
            child_index = parent_index * 2
            if self.nodes[parent_index].value > self.nodes[child_index].value:
                self.swap_two_nodes(parent_index, child_index)
                parent_index = child_index
            elif self.nodes[parent_index].value > self.nodes[child_index+1].value:
                self.swap_two_nodes(parent_index, child_index + 1)
                parent_index = child_index + 1
            else:
                break

    def deleteMin(self):
        self.swap_two_nodes(1, len(self.nodes) - 1)
        self.nodes = self.nodes[:-1]
        parent_index = 1
        self.swap_with_childrens(parent_index)

    def changeValue(self, node, value_to_change):
        # find node
        index = 1
        for n in self.nodes[1:]:
            if n.equals(node):
                break
            index += 1
        print(index)
        self.nodes[index].value = value_to_change
        self.swap_with_childrens(index)

if __name__ == "__main__":
    data = Heap()
    data.constructHeap([35, 33, 42, 10, 14, 19, 27, 44, 26, 31])

    data.changeValue(Node(10),45)
    for n in data.nodes:
        print(n.value)
