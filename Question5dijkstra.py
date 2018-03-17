# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 10:18:27 2018

@author: Xu Wen Tao
Dijkstra's shortest-path algorithm
"""
import numpy as np

#file_path = "./dijkstraDataTest.txt"
file_path = "./dijkstraData.txt"
with open(file_path, "r") as f:
    raw = f.read()
raw = raw.split("\n")
print(raw)
graph = {}
for x in raw[0:-1]: # the last element is a ''
    
    x = x.split('\t') # first element is vertices, followed by vetice,edge
    d = {v.split(',')[0]:int(v.split(',')[1]) for v in x[1:-1]}
    graph[x[0]] = d #graph is a dict of dict
        
#print(graph)
# initialize
visited = set(['1']) # the vertices processed so far
shortest_value = {'1':0} # computed shortest path distance
added_new = 1# flag to indicate the iteration is not done yet
while added_new:
    next_shortest_value = np.inf
    
    added_new = 0
    for vc, vd in graph.items():
        if vc in visited: # vc in graph X
            for v, d in vd.items():
                if v not in visited: # v in graph V-X
                    ds = d + shortest_value[vc]
                    if ds < next_shortest_value:
                        next_shortest_value = ds
                        next_shortest_vertice = v
                        from_vertice = vc
    # if we find a vertice not in visited, add the vertice with shortest path
    if next_shortest_value != np.inf:
        visited.add(next_shortest_vertice)
        shortest_value[next_shortest_vertice] = next_shortest_value
        added_new = 1
#        print("the next_shortest_vertice is: ", next_shortest_vertice)
#        print("the from_vertice is: ", from_vertice)
#        print("visited:", visited)

#print(shortest_value)
k = [7,37,59,82,99,115,133,165,188,197]
for v in k:
    v = str(v)
    try:
        print("the shortest path to {} is {}".format(v, shortest_value[v]))
    except KeyError: #vertice is not connecte to 1
        print("the shortest path to {} is {}".format(v, 1000000))
                        
                    
