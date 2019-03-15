import numpy as np
import os
import sys



line = np.array([line.rstrip("\n") for line in open("data.txt")])
data_origin = np.array([np.array(l.split("\t")).astype(int) for l in line])


def re_create_graph(graph, e, v):
    for g in graph:
        if g[0] != 0:
            mask = np.append([False], g[1:]==e)
            g[mask] = (v+1)

def create_dic(graph):
    dic = {}
    for g in graph:
        if g[0] != 0:
            dic[g[0]] = len(g[1:])
    return dic

def algo(data):
    count = 1
    # Merge vertices until only two vertices existed
    while count <= 198:

        # randomly choose 1 vertex in vertices space
        v = np.random.choice(len(data))

        if data[v][0] == 0:
            continue

        # randomly choose 1 vertex that is connected to v vertex
        e = np.random.choice(data[v][1:])

        # find index of e in v-th row
        e_index = np.argwhere(data[v]==e)
        # find index of v in e-th row
        v_index = np.argwhere(data[e-1]==(v+1))

        # remove edge between v and e
        data[v] = np.delete(data[v], e_index)
        data[e-1] = np.delete(data[e-1], v_index)

        # merge row v and e
        data[v] = np.append(data[v], data[e-1][1:])

        # remove row e
        data[e-1] = np.array([0])

        re_create_graph(data, e, v)
        count = count + 1

    return data

if __name__ == "__main__":
    lowest = 100
    for t in range(40000):
        data = algo(data_test)
        print(data_origin)
        dic = create_dic(data)

        for k,v in dic.items():
            if v < lowest:
                lowest = v
    print(lowest)
