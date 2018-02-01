# -*- coding: utf-8 -*-
"""
Created on Sat Jan 20 10:32:05 2018
graph is in the fomrmat of dict, with k vetices, and values all the outgoing edges 

@author: Xu Wen Tao
"""
import resource
from resource import setrlimit # this works only on unix, not on windows
from sys import setrecursionlimit 
# reach maximum recursion limit if graph is too large, increase the limit
setrecursionlimit(80000)
# default stack size not enought if graph is too large, increase the size
setrlimit(resource.RLIMIT_STACK, (10**10, 10**10)) 

def dfs(G, i, loop):
    '''
    :loop, if =1, then the first DFS, else the second DFS
    '''
    global t, s, leader
    explored.add(i) # mark i as explored  
    try:
        l = G[i]
        for w in l: # w is the outgoing arc
            if w not in explored:
                dfs(G, w, loop = loop)
    except KeyError:
        pass # w has not outgoing arc
    
    if loop == 1:           
        t+=1
        ft[t] = i
    else:
        header[leader-1] += 1
   
if __name__ == "__main__":
    
    with open("SCC.txt", 'r') as f:
        lines = f.read()
    lines = lines.split("\n")
    n = 0 # number of vetices
    g = {}
    gr = {} # reversed graph
    
    for line in lines:
        l = line.split(" ")
        #print(l)
        k = int(l[0])
        v = int(l[1])
        if k not in g:
            g[k] = [v]
        else:
            g[k].append(v)
        if v not in gr:
            gr[v] = [k]
        else:
            gr[v].append(k)
        if k > n:
            n = k
        if v > n:
            n = v
    
    global t, leader
    t = 0 #for finishing time in first pass
    ft = {} #finising time
    global s # for leaders in 2nd pass
    explored = set() # to mark explored
    print(n)
    for i in range(n, 0, -1): # from n down to 1
        if i not in explored: # i is not explored
            s = i # leader of that SCC
            dfs(gr, i, loop=1)
            
    explored = set()
    header=[0] * n # number of vertices in each leader
    for o in range(n, 0, -1):
        i = ft[o]
        leader = i # the leader in a SCC
        if i not in explored:
            #leader.append(o)
            dfs(g, i, 2)
 
    header.sort(reverse = True)
    print(header[:10]) # the top 10 largest SCC
        
    
    
    

