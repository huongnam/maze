#!/usr/bin/env python3
import sys
import collections


def find_path(maze, start, finish):
    ''' find the path from start to finish '''
    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if maze[y][x] == finish:
            return path
        for _x, _y in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if maze[_y][_x] != "#" and maze[_y][_x] not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and (_x, _y) not in seen:
                queue.append(path + [(_x, _y)])
                seen.add((_x, _y))


def move(pos, path):
    if pos[0] < path[1][0]:
        sys.stdout.write('MOVE RIGHT\n\n')
    elif pos[0] > path[1][0]:
        sys.stdout.write('MOVE LEFT\n\n')
    elif pos[1] < path[1][1]:
        sys.stdout.write('MOVE DOWN\n\n')
    elif pos[1] > path[1][1]:
        sys.stdout.write('MOVE UP\n\n')

s = sys.stdin.readline()
while s != "":
    if 'HELLO' in s:
        sys.stdout.write('I AM NAM\n\n')
    if 'YOU ARE' in s:
        name = s[-2]
        ''' get the letter attached to the IA '''
        sys.stdout.write('OK\n\n')
    if 'MAZE' in s:
        maze = []
        special_coin = []
        while len(s) > 0:
            s = input()
            maze.append(s)
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == name:
                    pos = (x, y)
                if maze[y][x] == "!":
                    special_coin.append((x, y))
        if special_coin:
            if len(find_path(maze, pos, "!")) <= 21:
                path = find_path(maze, pos, "!")
            else:
                path = find_path(maze, pos, "o")
        else:
            path = find_path(maze, pos, "o")
        move(pos, path)
    s = sys.stdin.readline()
