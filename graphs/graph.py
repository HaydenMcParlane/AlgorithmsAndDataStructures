#
#   Implementation of graph data structure for use with these
#   examples.
#
#   @author: Hayden McParlane

class GraphContract(object):

    def add_node(self, node):
        raise NotImplementedError()

    def nodes(self):
        raise NotImplementedError()

class UndirectedGraph(GraphContract):
    def __init__(self):
        self.nodes = dict()

    def add_node(self, node):
        if node is not None and node not in self.nodes():
            self.nodes.append(node)

    def add_edge(self, source_node, destination_node):
        if source_node not in self.nodes():
            self._nodes[source_node] = list()
        if destination_node not in self.nodes():
            self._nodes[destination_node] = list()
        self._nodes[source_node].append(destination_node)
        self._nodes[destination_node].append(source_node)

    def nodes(self):
        return self._nodes

class UndirectedTree(UndirectedGraph):
    pass