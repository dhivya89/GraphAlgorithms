import networkx as nx
import sys
import matplotlib.pyplot as plt

bo_dismissaldict = {}
bo_careeravgdict = {}
instrength = {}
gr = nx.DiGraph()
#ba_
def clean_data():
    line = lines.split('\t')
  #  print line
    try:
        if float(line[1]):
            ba_name = line[0]
            ba_careeravg = line[1]
            return ba_name
    except:
        bo_name = line[1]
        bo_dismissalno = line[3]
        bo2ba_avg = line[11]
        return bo_name,bo2ba_avg

#find career average for the respective bowler
def find_instrength():
    print "do"

    to_node_list =[]

    count = 0
    for to_node in gr.in_degree_iter():
    #print "yep"
        if (to_node[1]!=0):
          # print to_node[0]
           to_node_list.append(to_node[0])
           instrength[to_node[0]] = 0
           count = count + 1

    count = 0
    for edge in gr.edges():
        instrength[edge[1]] = instrength[edge[1]] + gr.get_edge_data(edge[0], edge[1])['weight']
    return instrength

#if __name__=='__main__':
#    main()
adjusted_weightof = {'NM Lyon': 0.7398684142790937, 'JL Pattinson': 0.06335405240758121, 'PM Siddle': 0.06279809310913335, 'XJ Doherty': 0.030480921208929514, 'MA Starc': 0.029292864146855103, 'GJ Maxwell': 0.029292864146855103, 'MC Henriques': 0.02616279070155214, 'SPD Smith': 0.018750000000000003}
for lines in open('F:\\Network Assignments\\PData\\careerbowler.txt','r'):
    line = lines.split('\t')
    bo_name = line[0]
    bo_avg = line[1]
    bo_careeravgdict[bo_name] = float(bo_avg)


for lines in open('F:\\Network Assignments\\PData\\comparebatting.txt','r'):
   result = clean_data()
   if len(result)!=2:
      current_batsman = result
      gr.add_node(current_batsman)
   else:
      bowler = result[0]
      bo2ba_avg = float(result[1])
      if not(gr.has_node(bowler)):
          gr.add_node(bowler)
      #calculate performance index for batsmen [ BAP = batting avg against bowler/bowler career avg ]
      BAP = (adjusted_weightof[bowler])*(bo2ba_avg/bo_careeravgdict[bowler])
      gr.add_edge(bowler,current_batsman,weight = BAP)

instrength = find_instrength()
batsman_gr = nx.DiGraph()


'''create batsman network (orginal if bo->ba1 and bo->ba2 make it ba1->ba2 based on instrength)
'''
batsmanlist_ofbow = {}
for key in bo_careeravgdict:
    batsmanlist_ofbow[key] = []
    for edges in gr.edges():
        if key == edges[0] :
            batsmanlist_ofbow[key].append(edges[1])
    len_batsmanlist = len(batsmanlist_ofbow[key])
    index = 0

    for index1 in range(0,len_batsmanlist-1):
        batsman1 = batsmanlist_ofbow[key][index1]
        if not(batsman_gr.has_node(batsman1)):
                batsman_gr.add_node(batsman1)
        for index2 in range(1,len_batsmanlist):
            batsman2 = batsmanlist_ofbow[key][index2]
            if not(batsman_gr.has_node(batsman2)):
                batsman_gr.add_node(batsman2)

            if instrength[batsman1] > instrength[batsman2]:
                if not(batsman_gr.has_edge(batsman2,batsman1)):
                   edges_weight = instrength[batsman1] - instrength[batsman2]
                   batsman_gr.add_edge(batsman2,batsman1)
            else:
                if not(batsman_gr.has_edge(batsman1,batsman2)):
                   edges_weight = instrength[batsman2] - instrength[batsman1]
                   batsman_gr.add_edge(batsman1,batsman2)

#nx.pagerank(batsman_gr)


number_of_batsman = batsman_gr.number_of_nodes()
pagerank_dict = nx.pagerank(batsman_gr)
sorted_pagerankdict = sorted(pagerank_dict.items(), key=lambda x: x[1])
adjusted_weightof = {}
index=0
for item in sorted_pagerankdict:
    index = index + 1
    #adjusted_weightof[item[0]] = 1/float(number_of_batsman)*index
    adjusted_weightof[item[0]] = item[1]

nx.write_gml(gr,"F:\\Network Assignments\\PData\\bowlertobat.gml")
gr.add_edge("JL Pattison","S Dhawan")
graph = nx.Graph(gr)


bowlerlist = []
for key in bo_careeravgdict:
    bowlerlist.append(key)
batsmanlist = batsman_gr.nodes()


pos = nx.spring_layout(graph)
nx.draw(graph,pos,with_labels=True)
'''for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]--!
'''
nx.draw_networkx_nodes(graph, pos, bowlerlist, node_size = 300, label = "community:",node_color = "green")
nx.draw_networkx_nodes(graph, pos, batsmanlist, node_size = 300, label = "community:",node_color = "red")
    #nx.draw_networkx_labels(graph,pos,)
#nx.
nx.draw_networkx_edges(graph,pos, alpha=0.5)
#plt.show()





