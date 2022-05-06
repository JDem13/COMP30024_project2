# -*- coding: utf-8 -*-
"""
Function determines if there is an ability to capture by colouring a
certain node. It takes arguments, board, board size n and current node
"""

from inPath import withinBounds as wb

def canCapture(board, n, node):
    
    row = node[row]
    column = node[column]
    label = node[label]
    canCapture = 1
    cannotCapture = 0
    
         
    #outer sandwich case
    if(wb(n,row+1,column-1)*wb(n,row+1,column)*wb(n,row+2,column-1)):
        if(board[(row+1,column-1)] != label):
            if(board[(row+1,column)] != label):
                if(board[(row+2,column-1)] == label):
                    return canCapture
    
    if(wb(n,row-1,column+1)*wb(n,row-1,column)*wb(n,row-2,column+1)):
        if(board[(row-1,column+1)] != label):
            if(board[(row-1,column)] != label):
                if(board[(row-2,column+1)] == label):
                    return canCapture
                
    if(wb(n,row+1,column)*wb(n,row,column+1)*wb(n,row+1,column+1)):
        if(board[(row+1,column)] != label):
            if(board[(row,column+1)] != label):
                if(board[(row+1,column+1)] == label):
                    return canCapture
                
    if(wb(n,row,column-1)*wb(n,row-1,column)*wb(n,row-1,column-1)):
        if(board[(row,column-1)] != label):
            if(board[(row-1,column)] != label):
                if(board[(row-1,column-1)] == label):
                    return canCapture    
                
    if(wb(n,row,column-1)*wb(n,row+1,column-1)*wb(n,row+1,column-2)):
        if(board[(row,column-1)] != label):
            if(board[(row+1,column-1)] != label):
                if(board[(row+1,column-2)] == label):
                    return canCapture
                
    if(wb(n,row,column+1)*wb(n,row+1,column)*wb(n,row+1,column+1)):
        if(board[(row,column+1)] != label):
            if(board[(row+1,column)] != label):
                if(board[(row+1,column+1)] == label):
                    return canCapture
            
    if(wb(n,row,column+1)*wb(n,row-1,column+1)*wb(n,row-1,column+2)):
        if(board[(row,column+1)] != label):
            if(board[(row-1,column+1)] != label):
                if(board[(row-1,column+2)] == label):
                    return canCapture
                
                
    #inner sandwhich
    
    if(wb(n,row,column-1)*wb(n,row+1,column-1)*wb(n,row-1,column)):
        if(board[(row-1,column)] != label):
            if(board[(row+1,column-1)] != label):
                if(board[(row,column-1)] == label):
                    return canCapture
            
    if(wb(n,row,column+1)*wb(n,row-1,column+1)*wb(n,row+1,column)):
        if(board[(row+1,column)] != label):
            if(board[(row-1,column+1)] != label):
                if(board[(row,column+1)] == label):
                    return canCapture
                
    if(wb(n,row+1,column)*wb(n,row+1,column-1)*wb(n,row,column+1)):
        if(board[(row,column+1)] != label):
            if(board[(row+1,column-1)] != label):
                if(board[(row+1,column)] == label):
                    return canCapture
                
    if(wb(n,row-1,column)*wb(n,row,column-1)*wb(n,row-1,column+1)):
        if(board[(row-1,column+1)] != label):
            if(board[(row,column-1)] != label):
                if(board[(row-1,column)] == label):
                    return canCapture
                
    if(wb(n,row+1,colum-1)*wb(n,row+1,column)*wb(n,row,column-1)):
        if(board[(row+1,column)] != label):
            if(board[(row,column-1)] != label):
                if(board[(row+1,column-1)] == label):
                    return canCapture
                
    if(wb(n,row-1,column+1)*wb(n,row,column+1)*wb(n,row-1,column)):
        if(board[(row,column+1)] != label):
            if(board[(row-1,column)] != label):
                if(board[(row-1,column+1)] == label):
                    return canCapture
                