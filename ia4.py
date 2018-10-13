#!/usr/bin/env python3
import sys
import collections

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

def find_path(maze, start):
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if maze[y][x] == "o":
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 < x2 < len(maze[0]) and 0 < y2 < len(maze) and maze[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


# def find_path(graph, start, end, path=[]):
#         path = path + [start]
#         if start == end:
#             return path
#         for node in graph[start]:
#             if node not in path:
#                 newpath = find_path(graph, node, end, path)
#                 if newpath: return newpath
# #
def move(pos, path):
    if pos[0] < path[1][0]:
        sys.stdout.write('MOVE RIGHT\n\n')
    elif pos[0] > path[1][0]:
        sys.stdout.write('MOVE LEFT\n\n')
    elif pos[1] < path[1][1]:
        sys.stdout.write('MOVE DOWN\n\n')
    elif pos[1] > path[1][1]:
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

        path = find_path(maze, pos)
        # f = open('hehe4', 'a')
        # f.write(str(path) + "\n")
        # f.close()



        move(pos, find_path(maze, pos))
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
