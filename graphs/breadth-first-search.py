from queue import Queue
from graph import Tree
from enum import Enum

def run(graph, source_node):
    initialize_nodes(graph)
    q = Queue()
    tree = Tree()
    color(source_node, Color.Grey)
    q.put(source_node)
    while not q.empty():
        current_node = q.get()
        for child in graph[current_node]:
            if child.color is Color.White:
                visit(child)
                color(child, Color.Grey)
                child.parent = current_node
                q.put(child)
            else:
                # TODO: processing logic here.
                pass
        tree.add(current_node)
        color(current_node, Color.Black)

def visit(node):
    # Do something useful. Right now this function
    # is just present for algorithmic clarity.
    print(node, node.color)

def initialize_nodes(graph):
    for node in graph.nodes():
        color(node, Color.White)

def color(node, new_color):
    setattr(node, "color", new_color)

class Color(Enum):
    White = "White"
    Grey = "Grey"
    Black = "Black"
