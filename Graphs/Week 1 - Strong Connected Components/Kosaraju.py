import numpy as np
import os
import sys

class kosaraju:
    def __init__(self, file):
        self._graph = {}
        self._graph_reversed = {}
        self._vertices = {}
        self._leaders = {}
        self._f_temp = {}
        self._f = {}
        self.t = 0
        self.s = None
        with open(file) as f:
            for count, line in enumerate(f):
                numbers = [int(number) for number in line.split()]
                for n in numbers:
                    # 0: unexplored
                    # 1: explored
                    self._vertices[n] = 0

                # Original Graph
                if numbers[0] not in self._graph.keys():
                    self._graph[numbers[0]] = [numbers[1]]
                else:
                    self._graph[numbers[0]].append(numbers[1])
                if numbers[1] not in self._graph.keys():
                    self._graph[numbers[1]] = []

                # Reverse Graph
                if numbers[1] not in self._graph_reversed.keys():
                    self._graph_reversed[numbers[1]] = [numbers[0]]
                else:
                    self._graph_reversed[numbers[1]].append(numbers[0])
                if numbers[0] not in self._graph_reversed.keys():
                    self._graph_reversed[numbers[0]] = []

        # initialize finishing time
        l = list(self._vertices.keys())
        l.sort()
        for t in range(len(l)):
            self._f_temp[t+1] = l[t]
        print(self._graph_reversed)

    def DFS(self, graph, i):
        self._vertices[i] = 1
        self._leaders[i] = self.s
        for j in graph[i]:

            if self._vertices[j] == 0:
                self.DFS(graph ,j)

        self.t += 1
        self._f[self.t] = i


    def DFS_loop(self, graph, f):
        self.unexplored()
        first = True
        for t in reversed(range(len(f.keys()))):

            i = f[t+1]

            if self._vertices[i] == 0:
                self.s = i
                self.DFS(graph, i)


    def unexplored(self):
        for k in self._vertices.keys():
            self._vertices[k] = 0

    def kasaraju(self):
        self.DFS_loop(self._graph_reversed, self._f_temp)
        self.DFS_loop(self._graph, self._f)

        SCCs = {}
        for node,leader in self._leaders.items():
            if leader not in SCCs.keys():
                SCCs[leader] = 1
            else:
                SCCs[leader] += 1
        l = []
        for value in SCCs.values():
            l.append(value)
        l.sort()
        print(l)





if __name__ == "__main__":

    k = kosaraju("data.txt")
    k.kasaraju()
