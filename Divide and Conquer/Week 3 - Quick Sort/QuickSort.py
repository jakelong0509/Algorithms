import numpy as np
import os
import sys

data = np.array([int(line.rstrip("\n")) for line in open("QuickSort_data.txt")])
data_test = np.array([3,5,4,2,1])
def Partition(data, l, r):


    p = data[l]

    i = l + 1
    for j in range(l + 1, r):
        if data[j] < p:
            data[j], data[i] = data[i], data[j]
            i = i + 1
    data[l], data[i - 1] = data[i - 1], data[l]
    p_index = i - 1
    return p_index

def QuickSort(data, n):
    if n <= 1:
        return
    l = 0
    p_index = Partition(data, l, n)
    QuickSort(data[:p_index], len(data[:p_index]))
    QuickSort(data[p_index+1:], len(data[p_index+1:]))

QuickSort(data, len(data))
print(data)
