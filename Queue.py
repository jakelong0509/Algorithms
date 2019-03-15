import numpy as np

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return_item = self.items[0]
        self.items = self.items[1:]
        return return_item
