import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
#import scipy.stats.norm as sc
graph = nx.Graph()

for lines in open('F:\Network Assignments\PData\IND_last4yrpartner.txt','r'):

    line = lines.split("\t")
    player = line[0]
    player1,player2=player.split(',\xc2\xa0')
    if not(graph.has_node(player1)):
        graph.add_node(player1)
    if not(graph.has_node(player2)):
        graph.add_node(player2)
    if not(graph.has_edge(player1,player2)):
        graph.add_edge(player1,player2)
degree_list = []
for node in graph.nodes():
    degree_list.append(nx.degree(graph,node))
    print str(nx.degree(graph,node))
'''n = graph.number_of_nodes()
frequency = np.histogram(degree_list,range(1,n+1), density=False)

pdf = {}
for i in range(0,n+1):
    pdf[i] = 0

for i in frequency[0]:
    pdf[i] += 1

sumOfInDegress = sum(pdf.values())
for i in range(0,len(pdf)):
    pdf[i] = pdf[i] * 1.0 / sumOfInDegress

cdf = []
cdf.append(pdf[0])
for i in range(1,(n+1)):
    cdf.append(cdf[i - 1] + pdf[i])

ccdf=[]
for i in range(0,(n+1)):
    ccdf.append(round((1 - cdf[i]),4))

x = []
y = []
for i in range(0,(n+1)):
    if ccdf[i] != 0.0:
        x.append(i)
        y.append(ccdf[i])
plt.loglog(x,y,'ro')

#sc.cdf(degree_list)'''


