from fastapi import FastAPI
from Utils.JSONCreator import getJsonFromArray

app = FastAPI()


@app.get("/get_data_structures")
async def datastructures():
    return getJsonFromArray(["stack", "queue", "array", "arraylist", "linkedlist", "tree", "trie", "graph"])

@app.get("/data_structure/{name}")
async def data_structure(name: str):
    if name == "stack": return "this is a stack. Stack is last in and first out"
    elif name == "queue": return "this is a queue. queue is first in and first out"
    elif name == "array": return "this is a array"
    elif name == "arraylist": return "this is a arraylist"
    elif name == "linkedlist": return "this is a linkedlist"
    elif name == "tree": return "this is a tree"
    else: return "this is not a data structure"