# -*- coding: utf-8 -*-



import math

MAX_LENGTH = 1000000

def shortestPath(node, goalNode, board, n):
    processed_data = process_input(board, n, node, goalNode)
    return traverse_board(processed_data)
    
    


def traverse_board(processed_data):
    lim = processed_data['lim']
    start = tuple(processed_data['start'])
    goal = tuple(processed_data['goal'])

    blocks = processed_data['pieces']

    # first move: expand start node 
    n0 = {'pos': start, 'cost': 0, 'parent': None}
    queue = [create_node(move, n0, goal) for move in 
        possible_moves(start, lim, blocks) if possible_moves(start, lim, blocks)]
    
    # lowest cost of all traversed, only add in a new node if not traversed OR it has a lower cost to what's in traversal list
    # then, update traversal list
    traversed = [] 

    while queue:
        node = get_lowest_node(queue)
        queue.remove(node)

        if (check_traversed(node, traversed)):
            continue 

        if (node['pos']== goal):
            last_node = node
            break

        moves = possible_moves(node['pos'], lim, blocks)
        queue += [create_node(move, node, goal) for move in moves]

    if queue:
        path_length = find_length(last_node, start)
    else:
        path_length = MAX_LENGTH


def find_length(last_node, start):
    node = last_node
    length = 0
    while (node['parent']):
        length += 1
        node = node['parent']
    length += 1
    return length

def check_traversed(node, traversed):
    found = False
    for each in traversed:
        if (node['pos'] == each['pos']):
            found = True
            if (node['cost'] < each['cost']):
                traversed.remove(each)
                found = False
   
    if (not found):
        traversed.append(node)

    return found
    

def get_lowest_node(queue):
    min_cost = 100000 # hard coded, change later 
    for each in queue:
        if (each['cost'] < min_cost):
            lowest_node = each
            min_cost = each['cost']
    
    assert(lowest_node)
    return lowest_node


def create_node(pos, parent, goal):
    cost = parent['cost']+heuristic(pos, goal)
    return {'pos': pos, 'cost': cost, 'parent': parent}

# heuristic!
def heuristic(pos1, pos2):
    return ((math.sqrt((pos1[0]-pos2[0])**2+(pos1[1]-pos2[1])**2)))

def possible_moves(pos, lim, occupied):
    # can go up a row, down a row, to the left, right, or diagonally left or right
    # maximum of 6 options 
    possible_moves = []
    possible_moves.append((pos[0]+1, pos[1]))
    possible_moves.append((pos[0]+1, pos[1]-1))
    possible_moves.append((pos[0]-1, pos[1]))
    possible_moves.append((pos[0]-1, pos[1]+1))
    possible_moves.append((pos[0], pos[1]+1))
    possible_moves.append((pos[0], pos[1]-1))
    possible_moves = [move for move in possible_moves if legal_move(move, lim, occupied)]
    return possible_moves

def legal_move(move, lim, occupied):
    if (move in occupied):
        return False
    if (move[0] < 0 or move [0] >= lim):
        return False
    if (move[1] < 0 or move[1] >= lim):
        return False 
    return True

def process_input(board, n, node, goal):
    pieces = []
    label = node[label]
    
    if (label =='r'):
        blocked = 'b'
    if (label == 'b'):
        blocked ='r'
        
    #find all blocked pieces
    for (row, column) in board.keys():
        if (board[(row, column)] == blocked):
            pieces.append((row,column))
        
        
    return {'start': [node[row], node[column]], 'goal': [goal[row], goal[column]],
            'pieces': pieces, 'lim': n}
    