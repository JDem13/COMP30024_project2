# -*- coding: utf-8 -*-
"""
Functions find the nodes in a path with shortest distance to the top goal
and bottom goal.

"""

MAX_LENGTH = 1000000

from inPath import withinBounds

def goalDistance(board, node, n, side):
    
    #find all available goal nodes 
    goalNodes = findGoalNodes(board, node, n, side)
    
    #evaluate current distance from current node to goal
    dist = shortestDist(node, goalNodes)
    
    #expand current node and enqueue expanded nodes
    queue = []
    visited = []
    [queue, visited] = expand(board, node, n, queue, visited)
    
    #find shortest path
    while(queue):
        
        [node, queue] = dequeue(queue)
        
        if (shortestDist(node, goalNodes) < dist):
            dist = shortestDist(node, goalNodes)
        
        
        [queue, visited] = expand(board, node, n, queue, visited)
    
    return dist
    
 
    
def findGoalNodes(board, node, n, side):
    
    label = node[label]
    goalNodes = []
    
    if (label == "b"):
        if (side == "top"):
            column = 0
        if (side == "bottom"):
            column = n
        for row in range(0,n+1):
            if (board[(row, column)] != "r" ):
                goalNodes.append((row,column))
    
    if (label == "r"):
        if (side == "top"):
            row = 0
        if (side == "bottom"):
            row = n
        for column in range(0,n+1):
            if (board[(row, column)] != "blue" ):
                goalNodes.append((row,column))
        
    return goalNodes
        
        
        
def shortestDist(node, goalNodes):
    
    dist = MAX_DISTANCE
    
    for goalNode in goalNodes:
        if (shortestPath(node, goalNode) < dist):
            dist = shortest_path(node, goalNode)
    
    return dist
       
        
def dequeue(queue):
    
    
    for key in queue:
        node = key
        queue.remove(node)
        break
       
     return [node, queue]   
 
    
 

def expand(board, node, n, queue, visited):
    
    row = node[row]
    column = node[column]
    label = node[label]
    
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            #check this isn't starting node
            if ~((i==0)&(j==0)):
                #check coordinates are within bounds
                if (withinBounds(n, row+i, column+j)):
                    #check expanded node has same label as root node
                    if(board[(row+i, column+j)] == label):
                        #check we haven't already visited this node
                        if ((row+i, column+j) not in visited):
                            #add node to queue and visited
                            visited.append((row+i, column+j))
                            queue.append({"row":row, "column":column,
                                          "label":label})
                            
    return [queue, visited]
                            
                    








        
        