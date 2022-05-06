# -*- coding: utf-8 -*-


""" 
Function isInPath evaluates if a certain node of interest is part of a 
path. 

It recieves as our node of interest, which has (row, column) coordinates and label. 
A board, being a dictionary with keys (row, column) coordinates and values {b,r,e}
respecrively meaning blue, red, empty. And board size n.

The outputs are 1 (in path) or 0 (not in path)
"""


def inPath(board, n, node):
    row = node[row]
    column = node[column]
    label = node[label]
    inPath = 0

    
    #check if node touches at least one node of same label
    for i in [-1,0,1]:
        for j in [-1,0,1]:
            #unless both i and j are zero
            if ~((i == 0)&(j == 0)):
                #check if coordinate is in bounds
                if withinBounds(n, row+i, column+j):
                    #check if node has same label
                    if (board[(row,column)] == board[(row+i, column+j)]):
                        inPath = 1
                        break
    return inPath


def withinBounds(n, row, column):
    
    withinBounds = 0
    if(0 <= row <= n):
        if (0 <= column <= n):
            withinBounds = 1
    
    return withinBounds
    
    
    
    
    