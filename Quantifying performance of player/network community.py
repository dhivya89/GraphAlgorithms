import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import community
#import scipy.stats.norm as sc
graph = nx.Graph()

for lines in open('F:\\Network Assignments\\Project\\IND_last4yrpartner.txt','r'):
    line = lines.split("\t")
    player = line[0]
    player1,player2=player.split(',\xc2\xa0')
    if not(graph.has_node(player1)):
        graph.add_node(player1)
    if not(graph.has_node(player2)):
        graph.add_node(player2)
    if not(graph.has_edge(player1,player2)):
        graph.add_edge(player1,player2)
degree_dict = {}
for node in graph.nodes():
    degree_dict[node]=nx.degree(graph,node)
partition = community.best_partition(graph)
modularity = community.modularity(partition,graph)
#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(graph)
count = 0.
nx.draw(graph,pos,with_labels=True)
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(graph, pos, list_nodes, node_size = 300, label = "community:",node_color = str(count / size))
    #nx.draw_networkx_labels(graph,pos,)
#nx.
nx.draw_networkx_edges(graph,pos, alpha=0.5)
plt.show()