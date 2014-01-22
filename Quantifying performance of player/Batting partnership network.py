#BATTING PARTNERSHIP NETWORK
import networkx as nx
import matplotlib.pyplot as plt
global_list = []
def calculate_weight(runs, total):
   # print runs, total
    return int(runs)/float(total)

def check_partnerexists(p1,p2,p1_runs,p2_runs,total_runs):
    count = 0
    for line in global_list:
        if line[0] == p1 and line[1] == p2 :
            return count, True
        count = count + 1
    return -1,False

def split_lines(lines):
    split_line = lines.split('\t')
    total_runs = float(split_line[1])
    if (total_runs == 0.0) :
        return
    player1 = split_line[5].split('(')
    #print player1
    p1_name = player1[0]
    p1_runs = int(player1[1].strip(')'))

  #  print p1_runs, total_runs

    player2 = split_line[6].split('(')
 #   print player2
    p2_name = player2[0]
    p2_runs = int(player2[1].strip(')'))

    if p1_name.split()[1] > p2_name.split()[1]:
        temp1,temp2 = p1_name,p1_runs
        p1_name,p1_runs = p2_name,p2_runs
        p2_name,p2_runs = temp1,temp2
    count,label = check_partnerexists(p1_name,p2_name,p1_runs,p2_runs,total_runs)
    #print label
    if (label==True):
        global_list[count][2] = global_list[count][2] + p1_runs
        global_list[count][3] = global_list[count][3] + p2_runs
        global_list[count][4] = global_list[count][4] + total_runs
        #add_runs(p1_name,p2_name,p1_runs,p2_runs,)
    else:
        global_list.append([p1_name,p2_name,p1_runs,p2_runs,total_runs])


gr = nx.DiGraph()
for lines in open('partnership.txt','r'):
    result = split_lines(lines)
for record in global_list :
    node1,node2,p1_runs,p2_runs,total_runs = record[0],record[1],record[2],record[3],record[4]
    wt21 = calculate_weight(p1_runs,total_runs)
    wt12 = calculate_weight(p2_runs,total_runs)
    '''if result:
        node1,weight_21,node2,weight_12,p1runs,p2runs,total = result'''
    if not(gr.has_node(node1)) and not(gr.has_node(node2)):
        gr.add_node(node1)
        gr.add_node(node2)
    elif not(gr.has_node(node1)):
        gr.add_node(node2)
    elif not(gr.has_node(node2)):
        gr.add_node(node1)
    gr.add_edge(node1,node2,weight = wt12)
    gr.add_edge(node2,node1,weight = wt21)
       # print gr.get_edge_data(node1,node2)

indegree = {}
pagerank = {}
betweenness = {}
closeness = {}
# Calculating indegree and stored in dictionary indegree{}
to_node_list =[]

count = 0
for to_node in gr.in_degree_iter():
    to_node_list.append(to_node[0])
    indegree[to_node[0]] = 0
    count = count + 1

count = 0
for edge in gr.edges():
    if (edge[0] == to_node_list[count]):
        indegree[to_node_list[count]] = indegree[to_node_list[count]] + gr.get_edge_data(edge[1], edge[0])['weight']
    else:
        count = count + 1
        if (edge[0] == to_node_list[count]):
           indegree[to_node_list[count]] = indegree[to_node_list[count]] + gr.get_edge_data(edge[1], edge[0])['weight']

nx.write_gml(gr,"F:\\Network Assignments\\Project\\test.gml")
edge_labels=dict([((u,v,),d['weight'])
             for u,v,d in gr.edges(data=True)])


#centrality measures
pagerank = nx.pagerank(gr,weight='weight')
betweenness = nx.betweenness_centrality(gr,weight='weight')
closeness = nx.closeness_centrality(gr)
# Drawing network
#gr = nx.Graph(data)
    #print total_runs, p1_name, p1_runs, p2_name,p2_runs
pos = nx.spring_layout(gr)
nx.draw(gr)#nx.draw_networkx_node
nx.draw_networkx_edge_labels(gr,pos,edge_labels=edge_labels)



#plt.show()'''