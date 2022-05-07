# -*- coding: utf-8 -*-
"""
Function determines if there is an ability to capture by colouring a
certain node. It takes arguments, board, board size n and current node
"""

from inPath import withinBounds as wb

def canCapture(board, n, node):
    
    row = node["row"]
    column = node["column"]
    label = node["label"]
    canCapture = 0
    capturedNodes= []
    
    if (label == "r"):
        opposite_label = "b"
    if (label == "b"):
        opposite_label ="r"
    
    
    
         
    #outer sandwich case
    if(wb(n,row+1,column-1)*wb(n,row+1,column)*wb(n,row+2,column-1)):
        if(board[(row+1,column-1)] == opposite_label):
            if(board[(row+1,column)] == opposite_label):
                if(board[(row+2,column-1)] == label):
                    canCapture = 1
                    capturedNodes.append((row+1,column-1), (row+1, column))
                    
    
    if(wb(n,row-1,column+1)*wb(n,row-1,column)*wb(n,row-2,column+1)):
        if(board[(row-1,column+1)] == opposite_label):
            if(board[(row-1,column)] == opposite_label):
                if(board[(row-2,column+1)] == label):
                    canCapture = 1
                    capturedNodes.append((row-1,column+1), (row-1, column))
                
    if(wb(n,row+1,column)*wb(n,row,column+1)*wb(n,row+1,column+1)):
        if(board[(row+1,column)] == opposite_label):
            if(board[(row,column+1)] == opposite_label):
                if(board[(row+1,column+1)] == label):
                    canCapture = 1
                    capturedNodes.append((row+1,column), (row, column+1))
                
    if(wb(n,row,column-1)*wb(n,row-1,column)*wb(n,row-1,column-1)):
        if(board[(row,column-1)] == opposite_label):
            if(board[(row-1,column)] == opposite_label):
                if(board[(row-1,column-1)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column-1), (row-1, column))    
                
    if(wb(n,row,column-1)*wb(n,row+1,column-1)*wb(n,row+1,column-2)):
        if(board[(row,column-1)] == opposite_label):
            if(board[(row+1,column-1)] == opposite_label):
                if(board[(row+1,column-2)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column-1), (row+1, column-1))
                
    if(wb(n,row,column+1)*wb(n,row+1,column)*wb(n,row+1,column+1)):
        if(board[(row,column+1)] == opposite_label):
            if(board[(row+1,column)] == opposite_label):
                if(board[(row+1,column+1)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column+1), (row+1, column))
            
    if(wb(n,row,column+1)*wb(n,row-1,column+1)*wb(n,row-1,column+2)):
        if(board[(row,column+1)] == opposite_label):
            if(board[(row-1,column+1)] == opposite_label):
                if(board[(row-1,column+2)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column+1), (row-1, column+1))
                
                
    #inner sandwhich
    
    if(wb(n,row,column-1)*wb(n,row+1,column-1)*wb(n,row-1,column)):
        if(board[(row-1,column)] == opposite_label):
            if(board[(row+1,column-1)] == opposite_label):
                if(board[(row,column-1)] == label):
                    canCapture = 1
                    capturedNodes.append((row-1,column), (row+1, column-1))
            
    if(wb(n,row,column+1)*wb(n,row-1,column+1)*wb(n,row+1,column)):
        if(board[(row+1,column)] == opposite_label):
            if(board[(row-1,column+1)] == opposite_label):
                if(board[(row,column+1)] == label):
                    canCapture = 1
                    capturedNodes.append((row+1,column), (row-1, column+1))
                
    if(wb(n,row+1,column)*wb(n,row+1,column-1)*wb(n,row,column+1)):
        if(board[(row,column+1)] == opposite_label):
            if(board[(row+1,column-1)] == opposite_label):
                if(board[(row+1,column)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column+1), (row+1, column-1))
                
    if(wb(n,row-1,column)*wb(n,row,column-1)*wb(n,row-1,column+1)):
        if(board[(row-1,column+1)] == opposite_label):
            if(board[(row,column-1)] == opposite_label):
                if(board[(row-1,column)] == label):
                    canCapture = 1
                    capturedNodes.append((row-1,column+1), (row, column-1))
                
    if(wb(n,row+1,column-1)*wb(n,row+1,column)*wb(n,row,column-1)):
        if(board[(row+1,column)] == opposite_label):
            if(board[(row,column-1)] == opposite_label):
                if(board[(row+1,column-1)] == label):
                    canCapture = 1
                    capturedNodes.append((row+1,column), (row, column-1))
                
    if(wb(n,row-1,column+1)*wb(n,row,column+1)*wb(n,row-1,column)):
        if(board[(row,column+1)] == opposite_label):
            if(board[(row-1,column)] == opposite_label):
                if(board[(row-1,column+1)] == label):
                    canCapture = 1
                    capturedNodes.append((row,column+1), (row-1, column))
    
    return [canCapture, capturedNodes] 
                
