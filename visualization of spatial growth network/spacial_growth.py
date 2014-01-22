from math import *
from random import *
import networkx as nx
import matplotlib.pyplot as plt


#initialize graph with 50 nodes
gr = nx.Graph()
for i in range(0,50):
   gr.add_node(i)
n = 50
pos_dict = {}
#assign point co-ordinates for every vertex
px = []
py = []
px.append(0.5)
py.append(0.5)
pos_dict[0] =(0.5,0.5)
s = sample(range(1,50),49)
for elem in s:
    px.append(elem*0.02)
s1 = sample(range(1,50),49)
for elem in s1:
    py.append(elem*0.02)
for i in range(1,50):
    pos_dict[i]=(px[i],py[i])


def calculate_euclidean_distance(p1x,p2x,p1y,p2y):
    eucliden_dist = pow(pow((p2x - p1x),2) + pow((p2y-p1y),2),0.5)
    return eucliden_dist

def distance_shortest_path(source,target):
    try:
       path_list = nx.shortest_path(gr,source,target)
    except:
        return 10000
    shortest_distance = 0
    for i in range(0,len(path_list)-1):
        new_d = calculate_euclidean_distance(px[path_list[i]],px[path_list[i+1]],py[path_list[i]],py[path_list[i+1]])
        shortest_distance = shortest_distance + new_d
    return shortest_distance

#for every pair of vertices, calculate minimum weight
def calculate_weight(alpha,v1,v2):

    dij = calculate_euclidean_distance(px[v1],px[v2],py[v1],py[v2])
    lj0 = distance_shortest_path(v2,0)
    di0 = calculate_euclidean_distance(px[v1],0.5,py[v1],0.5)
    #print alpha,v1,v2,px[v1],py[v1],di0
    weight = dij + alpha * ((dij+lj0)/float(di0))
    return weight



def find_vertices(alpha):
   min_wt = 1000000
   for i in disconnected_ver_list:
       for j in connected_ver_list:
           w = calculate_weight(alpha,i,j)
           if (w < min_wt): #and (j not in connected_ver_list):
             #  print i,j
               min_wt = w
               source = i
               target = j
   return source,target

#make edge from 0 to j and modify connected and disconnected lists
q_dict = {}
k = 1
for alpha in range(0,15):
   gr.remove_edges_from(gr.edges())
   disconnected_ver_list = []
   connected_ver_list = []
   connected_ver_list.append(0)
   for i in range(1,50):
      disconnected_ver_list.append(i)

   while(disconnected_ver_list):
       v1,v2 = find_vertices(alpha)
       gr.add_edge(v1,v2)

       connected_ver_list.append(v1)
       disconnected_ver_list.remove(v1)
   #draw network
   if alpha in [0,4,9,14]:
      plt.figure(k)
      k=k+1
      plt.title("alpha = "+str(alpha))
      #nx.draw(gr, cmap = plt.get_cmap('jet'))
      nx.draw(gr,pos = pos_dict)
   #calculate q - value
   sum = 0
   for i  in range(1,50):
       li0 =distance_shortest_path(i,0)
       di0 = calculate_euclidean_distance(px[i],0.5,py[i],0.5)
       sum = sum + li0/float(di0)
   q = (1/50.0)*(sum)
   q_dict[alpha] = q
plt.figure(5)
#plt.subplot(k*111)
plt.title("Route factor against weight function alpha")
plt.xlabel('alpha')
plt.ylabel('route factor q')
plt.plot(q_dict.keys(),q_dict.values())
plt.show()

