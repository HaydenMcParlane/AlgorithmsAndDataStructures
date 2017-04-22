from enum import Enum

# Initialize adjacency list
_GRAPH = None

class Node(object):
    def __init__(self, id):
        self.id = id

class Nodes(Enum):
    # A = "A"
    # B = "B"
    # C = "C"
    # D = "D"
    # E = "E"
    # F = "F"
    A = Node("A")
    B = Node("B")
    C = Node("C")
    D = Node("D")
    E = Node("E")
    F = Node("F")

def graph():
    return {
        Nodes.A: [Nodes.B, Nodes.C],
        Nodes.B: [Nodes.A, Nodes.F],
        Nodes.C: [Nodes.A, Nodes.B, Nodes.E, Nodes.D],
        Nodes.D: [Nodes.C, Nodes.E],
        Nodes.E: [Nodes.C, Nodes.D],
        Nodes.F: [Nodes.B]
    }

# def UndirectedEdge(object):
#     def __init__(self, nodeA, nodeB):
#         self.first = nodeA
#         self.second = nodeB
