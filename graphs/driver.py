#
#   This file is just to drive graph processing tests I'm doing
#   for experimentation with graph algorithms.
#
#   @author: Hayden McParlane
import networkx as nx
import matplotlib.pyplot as plot

def run(filename):
    pass
    # graph = nx.read_gml(filename)
    # for edge in graph.edges():
    #     print(edge)
    # pos = nx.spring_layout(graph)
    # nx.draw_networkx_nodes(graph, pos)
    # nx.draw_networkx_edges(graph, pos)
    # plot.show()

if __name__ == "__main__":
    run(r"./data/power.gml")
