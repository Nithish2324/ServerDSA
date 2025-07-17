from enum import Enum

class DataStructure(Enum):
    stack = "stack"
    queue = "queue"
    array = "array"
    arraylist = "arraylist"
    linkedlist = "linkedlist"
    tree = "tree"
    trie = "trie"
    graph = "graph"
    heap = "heap"
    hash = "hashmap"

    @property
    def id(self):
        return self.value

    @property
    def name(self):
        if self.value == "stack": return "Stack"
        elif self.value == "queue": return "Queue"
        elif self.value == "array": return "Array"
        elif self.value == "arraylist": return "Array List"
        elif self.value == "linkedlist": return "Linked List"
        elif self.value == "tree": return "Tree"
        elif self.value == "trie": return "Trie"
        elif self.value == "graph": return "Graph"
        elif self.value == "heap": return "Heap"
        elif self.value == "hashmap": return "Hash Map"
        else: return "Unknown"

