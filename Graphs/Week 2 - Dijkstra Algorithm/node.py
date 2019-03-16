import numpy as np
import sys
import os

class Node:
    def __init__(self, value):
        self.value = value
        self.vertex = None
        self.parent = None
        self.left = None
        self.right = None

    def swap(self):
        temp = self.value
        self.value = self.parent.value
        self.parent.value = temp
