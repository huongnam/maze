#!/usr/bin/env python3
import sys

# print("I AM IA\n\n")
# print("OK\n\n")
# maze = []
#
#
# for i in range(len(maze)):
#     line = sys.stdin.readline()
#     maze.append(line)
# print(''.join(maze))



def distance(x1, y1, x2, y2):
    b = (abs(x1 - x2) + abs(y1 - y2))
    # f = open('hehe1', 'a')
    # f.write(str(b) + "\n")
    # f.close()
    return b
def min_distance(pos, resource):
    a = min((distance(pos[0], pos[1], i[0], i[1]) for i in resource))
    # f = open('hehe', 'a')
    # f.write(str(a) + "\n")
    # f.close()
    return a

def get_target(pos, resource):
    for i in resource:
        if distance(pos[0], pos[1], i[0], i[1]) == min_distance(pos, resource):
            target = (i[0], i[1])
            # f = open('hehe2', 'a')
            # f.write(str(target) + "\n")
            # f.close()
            return target

def valid_move(empty_pos):
    graph = {}

    arcs_pos = []
    if pos[0] == 1: #left border
        if pos[1] == 1: #top left
            if maze[pos[1]][pos[0] + 1] == " ": #right
                arcs_pos.append(((pos[0] + 1), pos[1]))
            if maze[pos[1] + 1][pos[0]] == " ": #down
                arcs_pos.append((pos[0], (pos[1] + 1)))
        elif pos[1] == len(maze): #bottom left
            if maze[pos[1]][pos[0] + 1] == " ": #right
                arcs_pos.append(((pos[0] + 1), pos[1]))
            if maze[pos[1] - 1][pos[0]] == " ": #up
                arcs_pos.append((pos[0], (pos[1] - 1)))
        else:
            if maze[pos[1]][pos[0] + 1] == " ": #right
                arcs_pos.append(((pos[0] + 1), pos[1]))
            if maze[pos[1] - 1][pos[0]] == " ": #up
                arcs_pos.append((pos[0], (pos[1] - 1)))
            if maze[pos[1] + 1][pos[0]] == " ": #down
                arcs_pos.append((pos[0], (pos[1] + 1)))

    elif pos[0] == len(maze[len(maze) - 1]): #right border
        if pos[1] == 1: #top right
            if maze[pos[1]][pos[0] - 1] == " ": #left
                arcs_pos.append(((pos[0] - 1), pos[1]))
            if maze[pos[1] + 1][pos[0]] == " ": #down
                arcs_pos.append((pos[0], (pos[1] + 1)))
        elif pos[1] == len(maze): #bottom right
            if maze[pos[1]][pos[0] - 1] == " ": #left
                arcs_pos.append(((pos[0] - 1), pos[1]))
            if maze[pos[1] - 1][pos[0]] == " ": #up
                arcs_pos.append((pos[0], (pos[1] - 1)))

    elif pos[1] == 1: #top border
        if maze[pos[1]][pos[0] + 1] == " ": #right
            arcs_pos.append(((pos[0] + 1), pos[1]))
        if maze[pos[1]][pos[0] - 1] == " ": #left
            arcs_pos.append(((pos[0] - 1), pos[1]))
        if maze[pos[1] + 1][pos[0]] == " ": #down
            arcs_pos.append((pos[0], (pos[1] + 1)))

    elif pos[1] == len(maze): #bottom border
        if maze[pos[1]][pos[0] + 1] == " ": #right
            arcs_pos.append(((pos[0] + 1), pos[1]))
        if maze[pos[1]][pos[0] - 1] == " ": #left
            arcs_pos.append(((pos[0] - 1), pos[1]))
        if maze[pos[1] - 1][pos[0]] == " ": #up
            arcs_pos.append((pos[0], (pos[1] - 1)))

    else:
        if maze[pos[1]][pos[0] + 1] == " ": #right
            arcs_pos.append(((pos[0] + 1), pos[1]))
        if maze[pos[1]][pos[0] - 1] == " ": #left
            arcs_pos.append(((pos[0] - 1), pos[1]))
        if maze[pos[1] + 1][pos[0]] == " ": #down
            arcs_pos.append((pos[0], (pos[1] + 1)))
        if maze[pos[1] - 1][pos[0]] == " ": #up
            arcs_pos.append((pos[0], (pos[1] - 1)))
    graph[pos] = arcs_pos

    for i in empty_pos:
        arcs = []
        if i[0] == 1: #left border
            if i[1] == 1: #top left
                if maze[i[1]][i[0] + 1] == " ": #right
                    arcs.append(((i[0] + 1), i[1]))
                if maze[i[1] + 1][i[0]] == " ": #down
                    arcs.append((i[0], (i[1] + 1)))
            elif i[1] == len(maze): #bottom left
                if maze[i[1]][i[0] + 1] == " ": #right
                    arcs.append(((i[0] + 1), i[1]))
                if maze[i[1] - 1][i[0]] == " ": #up
                    arcs.append((i[0], (i[1] - 1)))
            else:
                if maze[i[1]][i[0] + 1] == " ": #right
                    arcs.append(((i[0] + 1), i[1]))
                if maze[i[1] - 1][i[0]] == " ": #up
                    arcs.append((i[0], (i[1] - 1)))
                if maze[i[1] + 1][i[0]] == " ": #down
                    arcs.append((i[0], (i[1] + 1)))

        elif i[0] == len(maze[len(maze) - 1]): #right border
            if i[1] == 1: #top right
                if maze[i[1]][i[0] - 1] == " ": #left
                    arcs.append(((i[0] - 1), i[1]))
                if maze[i[1] + 1][i[0]] == " ": #down
                    arcs.append((i[0], (i[1] + 1)))
            elif i[1] == len(maze): #bottom right
                if maze[i[1]][i[0] - 1] == " ": #left
                    arcs.append(((i[0] - 1), i[1]))
                if maze[i[1] - 1][i[0]] == " ": #up
                    arcs.append((i[0], (i[1] - 1)))

        elif i[1] == 1: #top border
            if maze[i[1]][i[0] + 1] == " ": #right
                arcs.append(((i[0] + 1), i[1]))
            if maze[i[1]][i[0] - 1] == " ": #left
                arcs.append(((i[0] - 1), i[1]))
            if maze[i[1] + 1][i[0]] == " ": #down
                arcs.append((i[0], (i[1] + 1)))

        elif i[1] == len(maze): #bottom border
            if maze[i[1]][i[0] + 1] == " ": #right
                arcs.append(((i[0] + 1), i[1]))
            if maze[i[1]][i[0] - 1] == " ": #left
                arcs.append(((i[0] - 1), i[1]))
            if maze[i[1] - 1][i[0]] == " ": #up
                arcs.append((i[0], (i[1] - 1)))

        else:
            if maze[i[1]][i[0] + 1] == " ": #right
                arcs.append(((i[0] + 1), i[1]))
            if maze[i[1]][i[0] - 1] == " ": #left
                arcs.append(((i[0] - 1), i[1]))
            if maze[i[1] + 1][i[0]] == " ": #down
                arcs.append((i[0], (i[1] + 1)))
            if maze[i[1] - 1][i[0]] == " ": #up
                arcs.append((i[0], (i[1] - 1)))
        graph[i] = arcs
    f = open('hehe3', 'a')
    f.write(str(graph) + "\n")
    f.close()
    return graph

def find_path(graph, start, end, path=[]):

    path = path + [start]
    if start == end:
        return path
    
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None

def move(pos, target):
    if pos[0] < target[0]:
        sys.stdout.write('MOVE RIGHT\n\n')
    elif pos[0] > target[0]:
        sys.stdout.write('MOVE LEFT\n\n')
    elif pos[1] < target[1]:
        sys.stdout.write('MOVE DOWN\n\n')
    elif pos[1] > target[1]:
        sys.stdout.write('MOVE UP\n\n')

while True:
    s = sys.stdin.readline()
    if 'HELLO' in s:
        sys.stdout.write('I AM NAM\n\n')
    if 'YOU ARE' in s:
        name = s[-2]
        sys.stdout.write('OK\n\n')
    if 'MAZE' in s:
        maze = []
        while len(s) > 0:
            s = input()

            maze.append(s)
        coin = []
        special_coin = []
        empty_pos = []


        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == name:
                    pos = (x, y)
                if maze[y][x] == "o":
                    coin.append((x, y))
                if maze[y][x] == "!":
                    special_coin.append((x, y))
                if maze[y][x] == " ":
                    empty_pos.append((x, y))
        f = open('hehe4', 'a')
        f.write(str(empty_pos) + "\n")
        f.close()
        valid_move(empty_pos)
        g = find_path(valid_move(empty_pos), (1,3), (3, 6), path=[])
        f = open('hehe5', 'a')
        f.write(str(g) + "\n")
        f.close()
        # f = open('debug', 'a')
        # f.write('current pos: ' + str(pos) + '\n')
        # f.write('coin pos: ' + str(coin) + '\n')
        # f.write('target: ' + str(get_target(pos, coin)) + '\n')
        # f.close()



        # if special_coin != "":
        #     min_distance(pos, special_coin)
        #     move(pos, get_target(pos, special_coin))
        # else:
        #     min_distance(pos, coin)
        #     move(pos, get_target(pos, coin))
        # valid_move(empty_pos)
        # graph = valid_move(empty_pos)
        # g = find_path(graph, coin[0], (1,1))
        # f = open('hehe6', 'a')
        # f.write(str(g) + "\n")
        # f.close()
        f = open('hehe7', 'a')
        f.write(str(len(maze)) + "\n")
        f.close()

        f = open('hehe8', 'a')
        f.write(str(pos) + "\n")
        f.close()
        # for i in coin:
        #     find_path(graph, pos, i)
        #     f = open('hehe5', 'a')
        #     f.write(str(find_path(graph, pos, i)) + "\n")
        #     f.close()
        # if special_coin != []:
        #     min_distance(pos, special_coin)
        #     move(pos, get_target(pos, special_coin))
        # else:
        #     min_distance(pos, coin)
        #     move(pos, get_target(pos, coin))




        # while len(s) > 0:
        #     s = input()
        #     f = open('getmaze', 'w')
        #     f.write(s + "\n")
        #     f.close()

        # f = open('getmaze', 'r')
        # line = f.readline()
        # while line:
        #     l.append(line)
        #     line = f.readline()
        # f.close()
print("name")
