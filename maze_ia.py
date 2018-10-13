#!/usr/bin/env python3
import sys
import collections

def find_path(maze, start, resource):

    queue = collections.deque([[start]])
    seen = set([start])
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if maze[y][x] == resource:
            return path
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 < x2 < len(maze[0]) and 0 < y2 < len(maze) and maze[y2][x2] != '#' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))


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
        if special_coin != []:
            path = find_path(maze, pos, "!")
        else:
            path = find_path(maze, pos, "o")
        move(pos, path)
