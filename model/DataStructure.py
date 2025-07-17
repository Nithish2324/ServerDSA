from dataclasses import dataclass
from typing import Dict, List, Optional

from model.DataStructureType import DataStructureType


@dataclass
class TimeComplexity:
    access: str
    search: str
    insertion: str
    deletion: str

@dataclass
class Complexity:
    time: TimeComplexity
    space: str

@dataclass
class DataStructure:
    name: str
    description: str
    real_world_examples: List[str]
    type: str
    operations: List[str]
    advantages: List[str]
    disadvantages: List[str]
    complexity: Complexity

STACK = DataStructure(
    name="Stack",
    description="A linear data structure following LIFO principle",
    real_world_examples=["Undo feature", "Browser history"],
    type="Linear",
    operations=["push", "pop", "peek"],
    advantages=["Easy to implement", "Efficient memory use"],
    disadvantages=["Fixed size in arrays", "Overflow/Underflow"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(n)",
            search="O(n)",
            insertion="O(1)",
            deletion="O(1)"
        ),
        space="O(n)"
    )
)

QUEUE = DataStructure(
    name="Queue",
    description="A linear data structure following FIFO principle",
    real_world_examples=["Ticket counter", "CPU scheduling"],
    type="Linear",
    operations=["enqueue", "dequeue", "peek"],
    advantages=["Order preservation", "Flexible size"],
    disadvantages=["Slower for random access"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(n)",
            search="O(n)",
            insertion="O(1)",
            deletion="O(1)"
        ),
        space="O(n)"
    )
)

ARRAY = DataStructure(
    name="Array",
    description="A fixed-size collection of elements stored in contiguous memory",
    real_world_examples=["Leaderboard scores", "Image pixels"],
    type="Linear",
    operations=["access", "insert", "delete", "search"],
    advantages=["Fast random access", "Memory efficiency"],
    disadvantages=["Fixed size", "Costly insertions/deletions"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(1)",
            search="O(n)",
            insertion="O(n)",
            deletion="O(n)"
        ),
        space="O(n)"
    )
)

ARRAYLIST = DataStructure(
    name="ArrayList",
    description="A resizable array that grows dynamically",
    real_world_examples=["Shopping cart items", "Dynamic playlists"],
    type="Linear",
    operations=["add", "remove", "get", "resize"],
    advantages=["Flexible size", "O(1) amortized insertion"],
    disadvantages=["Slower than static arrays", "Memory overhead"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(1)",
            search="O(n)",
            insertion="O(1)*",
            deletion="O(n)"
        ),
        space="O(n)"
    )
)

LINKEDLIST = DataStructure(
    name="LinkedList",
    description="A linear collection of nodes linked by pointers",
    real_world_examples=["Music playlists", "Browser history (back/forward)"],
    type="Linear",
    operations=["insert", "delete", "traverse", "reverse"],
    advantages=["Dynamic size", "Efficient insertions/deletions"],
    disadvantages=["Slow random access", "Extra memory for pointers"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(n)",
            search="O(n)",
            insertion="O(1)",
            deletion="O(1)"
        ),
        space="O(n)"
    )
)

TREE = DataStructure(
    name="Tree",
    description="A hierarchical structure with a root node and subtrees",
    real_world_examples=["File systems", "Organization charts"],
    type="Non-Linear",
    operations=["insert", "delete", "traverse (in-order, pre-order, post-order)", "search"],
    advantages=["Fast search (O(log n) for balanced trees)", "Hierarchical data representation"],
    disadvantages=["Complex balancing (for AVL/Red-Black trees)", "Memory overhead"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(log n)",
            search="O(log n)",
            insertion="O(log n)",
            deletion="O(log n)"
        ),
        space="O(n)"
    )
)

GRAPH = DataStructure(
    name="Graph",
    description="A collection of nodes (vertices) connected by edges",
    real_world_examples=["Social networks", "Google Maps"],
    type="Non-Linear",
    operations=["BFS", "DFS", "shortest path", "cycle detection"],
    advantages=["Models real-world networks", "Versatile"],
    disadvantages=["Complex algorithms", "Storage overhead (O(V+E))"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(1) (adjacency list)",
            search="O(V+E)",
            insertion="O(1)",
            deletion="O(1)"
        ),
        space="O(V+E)"
    )
)

HEAP = DataStructure(
    name="Heap",
    description="A complete binary tree where parent nodes dominate children (min/max)",
    real_world_examples=["Priority queues", "Job scheduling"],
    type="Non-Linear",
    operations=["insert", "extract-min/max", "heapify"],
    advantages=["Efficient priority operations", "O(1) min/max access"],
    disadvantages=["Slow search (O(n))", "Not cache-friendly"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(1)",
            search="O(n)",
            insertion="O(log n)",
            deletion="O(log n)"
        ),
        space="O(n)"
    )
)

HASHMAP = DataStructure(
    name="Hashmap",
    description="A key-value store using hash functions for O(1) average access",
    real_world_examples=["Python dictionaries", "Database indexing"],
    type="Linear (with collisions)",
    operations=["put", "get", "delete", "resize"],
    advantages=["Average O(1) operations", "Flexible keys"],
    disadvantages=["Worst-case O(n) time", "Memory overhead"],
    complexity=Complexity(
        time=TimeComplexity(
            access="O(1)*",
            search="O(1)*",
            insertion="O(1)*",
            deletion="O(1)*"
        ),
        space="O(n)"
    )
)


DATA_STRUCTURES = {
    DataStructureType.stack: STACK,
    DataStructureType.queue: QUEUE,
    DataStructureType.array: ARRAY,
    DataStructureType.arraylist: ARRAYLIST,
    DataStructureType.linkedlist: LINKEDLIST,
    DataStructureType.tree: TREE,
    DataStructureType.graph: GRAPH,
    DataStructureType.heap: HEAP,
    DataStructureType.hashmap: HASHMAP
}

def getDataStructure(dataStructureType: DataStructureType) -> Optional[DataStructure]:
    return DATA_STRUCTURES.get(dataStructureType)
