import networkx as nx


bo_dismissaldict = {}
bo_careeravgdict = {}
ba_careeravgdict = {}
instrength = {}
gr = nx.DiGraph()
#ba_
def clean_data():
    line = lines.split('\t')
    #print float(line[1])
    try:
        if float(line[1]):
            ba_name = line[0]
            ba_careeravg = line[1]
            ba_careeravgdict[ba_name] = float(ba_careeravg)
            return ba_name
    except:
        bo_name = line[1]
        bo2ba_dismissal = line[3]
        bo2ba_avg = line[11]
        return bo_name,bo2ba_dismissal

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
adjusted_weightof = {'AM Rahane': 0.03135561167192092,
 'B Kumar': 0.040433602731183814,
 'CA Pujara': 0.12314708669071994,
 'Harbhajan Singh': 0.02227503781217027,
 'I Sharma': 0.023973134849545132,
 'M Vijay': 0.06500749659217328,
 'MS Dhoni': 0.032213489963542924,
 'PP Ojha': 0.02598073725966883,
 'R Ashwin': 0.04939264431587652,
 'RA Jadeja': 0.028394248356822634,
 'S Dhawan': 0.19041238881190758,
 'SR Tendulkar': 0.08252731830199621,
 'V Kohli': 0.2141688459058154,
 'V Sehwag': 0.07071835673665659}

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
      bo2ba_dismissal = float(result[1])
      if not(gr.has_node(bowler)):
          gr.add_node(bowler)
      #calculate performance index for batsmen [ BAP = batting avg against bowler/bowler career avg ]
      BOP = adjusted_weightof[current_batsman]*bo2ba_dismissal*(ba_careeravgdict[current_batsman]/bo_careeravgdict[bowler])
      gr.add_edge(current_batsman,bowler,weight = BOP)

instrength = find_instrength()
bowler_gr = nx.DiGraph()

'''create batsman network (orginal if bo->ba1 and bo->ba2 make it ba1->ba2 based on instrength)
'''
bowlerlist_ofbat = {}
for key in ba_careeravgdict:
    bowlerlist_ofbat[key] = []
    for edges in gr.edges():
        if key == edges[0] :
            bowlerlist_ofbat[key].append(edges[1]) #bowler list of every batsman
    len_bowlerlist = len(bowlerlist_ofbat[key])
    #index = 0
#one mode projection within bowlers
    for index1 in range(0,len_bowlerlist-1):
        bowler1 = bowlerlist_ofbat[key][index1]
        if not(bowler_gr.has_node(bowler1)):
                bowler_gr.add_node(bowler1)
        for index2 in range(1,len_bowlerlist):
            bowler2 = bowlerlist_ofbat[key][index2]
            if not(bowler_gr.has_node(bowler2)):
                bowler_gr.add_node(bowler2)
#compare instrength and add links
            if instrength[bowler1] > instrength[bowler2]:
                if not(bowler_gr.has_edge(bowler2,bowler1)):
                   edges_weight = instrength[bowler1] - instrength[bowler2]
                   bowler_gr.add_edge(bowler2,bowler1)
            else:
                if not(bowler_gr.has_edge(bowler1,bowler2)):
                   edges_weight = instrength[bowler2] - instrength[bowler1]
                   bowler_gr.add_edge(bowler1,bowler2)

number_of_bowlers = bowler_gr.number_of_nodes()
pagerank_dict = nx.pagerank(bowler_gr)
sorted_pagerankdict = sorted(pagerank_dict.items(), key=lambda x: x[1])
adjusted_weightof = {}
index=0
for item in sorted_pagerankdict:
    index = index + 1
    #adjusted_weightof[item[0]] = 1/float(number_of_bowlers)*index
    adjusted_weightof[item[0]] = item[1]
print sorted_pagerankdict
print adjusted_weightof








