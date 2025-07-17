from enum import Enum

class DataStructureType(Enum):
    stack = "stack"
    queue = "queue"
    array = "array"
    arraylist = "arraylist"
    linkedlist = "linkedlist"
    tree = "tree"
    graph = "graph"
    heap = "heap"
    hashmap = "hashmap"

    @property
    def id(self):
        return self.value

