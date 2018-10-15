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




#
def valid_move(empty_pos, pos, end):
    graph = {}
    arcs1 = []
    direction = [(1, 0), (-1, 0), (0, 1), (0, - 1)]
    for i in direction:
        available_pos = (pos[0] + i[0], pos[1] + i[1])
        if available_pos in empty_pos:
            arcs1.append(available_pos)
    graph[pos] = arcs1
    while end not in graph.items():
        for key, values in graph.items():
            for value in values:
                if value not in graph.keys():
                    for j in direction:
                        arcs = []
                        available_pos = (value[0] + j[0], value[1] + j[1])
                        if available_pos in empty_pos:
                            arcs.append(available_pos)
                    graph[value] = arcs
    f = open('hehe2', 'a')
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

# def move(pos, target):
#     if pos[0] < target[0]:
#         sys.stdout.write('MOVE RIGHT\n\n')
#     elif pos[0] > target[0]:
#         sys.stdout.write('MOVE LEFT\n\n')
#     elif pos[1] < target[1]:
#         sys.stdout.write('MOVE DOWN\n\n')
#     elif pos[1] > target[1]:
#         sys.stdout.write('MOVE UP\n\n')

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


        t = valid_move(empty_pos, (1, 5), (3, 6))

        f = open('hehe3', 'a')
        f.write(str(t) + "\n")
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
