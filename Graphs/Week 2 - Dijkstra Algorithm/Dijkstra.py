import numpy as np
import os
import sys
from heap import Heap

class Dijkstra:
    def __init__(self, file):
        self._graph = {}
        self.A = {}
        self.X = []
        self.V = []
        self.dimension = None
        with open(file) as f:
            for count, line in enumerate(f):
                # line_arr[0] is tail vertex
                # 80,982: 80 is head vertex, 982 is edge length from tail to head
                line_arr = [elm for elm in line.split()]
                tail = line_arr[0]
                self.V.append(tail)
                for el in line_arr[1:]:
                    head, length = el.split(",")
                    self._graph[(int(tail), int(head))] = int(length)

        self.dimension = len(self.V)

    def shortest_path(self, f, t):
        self.X.append(f)
        self.A[f] = 0
        while True:
            w_star = None
            v_star = None
            smallest = float('inf')
            for s in self.X:
                for k, v in self._graph.items():
                    tail, head = k
                    if tail == s and head not in self.X:
                        temp = self.A[tail] + v
                        if temp < smallest:
                            smallest = temp
                            w_star = head
                            v_star = tail


            self.X.append(w_star)
            self.A[w_star] = self.A[v_star] + self._graph[(v_star, w_star)]
            if w_star == t:
                break

        print(self.A[w_star])



if __name__ == "__main__":
    vertices = [7,37,59,82,99,115,133,165,188,197]
    for t in vertices:
        graph = Dijkstra("data.txt")
        graph.shortest_path(1, t)
