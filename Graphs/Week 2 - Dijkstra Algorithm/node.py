import numpy as np
import sys
import os

class Node:
    def __init__(self, value):
        self.value = value
        #self.vertex = verte

    def equals(self, other_node):
        if self.value == other_node.value:
            return True
        else:
            return False
