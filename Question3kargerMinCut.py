# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:32:05 2018

@author: Xu Wen Tao
"""
import numpy as np
import copy
import random
def kargerMinCut(g, n):
    ''' given list representation of graph, find minumim cut
    :g, dict, the list representation of graph in dict format for calculation efficiency
    :n, integer, the number of random trials
    '''
    # assume there are at leat 2 vetices
    if len(g) == 2:
        for k, v in g.items():
            return len(v)
    minCut = np.inf 
    for i in range(n):
        graph = copy.deepcopy(g) # 
        np.random.seed(i) # define a different random seed each time
        while len(graph) > 2:
            veti1, veti2 = weightedPick(graph)
            #print("veti1 and veti2: ", veti1, veti2)
            for edge in graph[veti2]:
                # before combine veti2 to veti1, add veti1 to all veti2' connection 
                if edge != veti1:
                    #print(graph)
                    num_conn_to_veti2 = 0
                    l = []
                    for x in graph[edge]:
                        # remove all connection the veti2 and count the number of veti2
                        if x == veti2:
                            num_conn_to_veti2 += 1 
                        else: 
                            l.append(x)
                    # add the same number of veti1 to the vertice 
                    graph[edge] = l + [veti1] * num_conn_to_veti2 # add connection to veti1
            # add all veti2's connection to veti1, be sure to delete veti1 from the list(selft loop)
            l = graph[veti1] + graph[veti2]
            l = [x for x in l if (x != veti1 and x != veti2)]
            graph[veti1] = l
            # all veti2's realtion are transfered to veti1, delete veti1 
            graph.pop(veti2)
            #print(graph)
        # only two vetices left
        #print(graph)
        k1, k2 = list(graph)
        edge_num = len(graph[k1])
        if edge_num == len(graph[k2]): # make sure last two values have same length
            if edge_num < minCut:
                minCut = edge_num
        else: 
            return 
    print("one of the final graph after cutting: ", graph)
    return minCut
           
def weightedPick(g):
    ''' given a dict, with values list,  select a key randomly with weight proportional
    to the length of their corresponding list
    :return a ranoom key and a random value from its corresponding list
    '''
    g1 = {}
    for k, v in g.items():
        g1[k] = len(v)
    total = sum(g1.values())
    pick = random.randint(0, total-1)
    tmp = 0
    for k, weight in g1.items():
         tmp += weight
         if pick < tmp:
             break
    v = random.choice(g[k])
    return k, v

if __name__ == "__main__":
    
    with open("kargerMinCut.txt", 'r') as f:
        lines = f.readlines()
    
    gd = {}
    for line in lines:
        l = line.split("\t")
        l = [int(x) for x in l[0:-1]]
        gd[l[0]] = l[1:]
    #print(gd)
    N = len(gd)
    # probabilty of fail <= 1/N, in fact, with trials_num = 200, got the right answer
    # then try trials_num = 40000, takes quite a long time. 
    trials_num = int(N**2*np.log(N)) # probabilty of fail <= 1/N
    print(trials_num)
    final_min_cut = kargerMinCut(gd, trials_num)
    print(final_min_cut)

    
    

