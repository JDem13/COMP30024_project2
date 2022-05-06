# -*- coding: utf-8 -*-


WEIGHT_1 = 0
WEIGHT_2 = 0

from canCapture import canCapture
from goalPathHeuristics import goalDistance

def heuristic(board, node, n):
    
    heuristic = 0
    
    
    distance_top = goalDistance(board, node, n, "top")
    distance_bottom = goalDistance(board, node, n, "bottom")
    
    can_capture = canCapture(board, n, node)
    
    return = (WEIGHT_1 * (1/(distance_top + distance_bottom)) + 
              WEIGHT_2*can_capture)
    
    
    

