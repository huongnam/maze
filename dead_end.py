#!/usr/bin/env python3
import sys


def find_start(maze):
    if ' ' in maze[0]:
        return (maze[0].index(' '), 0)
    else:
        for i in range(len(maze)):
            if ' ' in maze[i][0]:
                return (maze[i].index(' '), i)


def find_finish(maze):
    return (maze[len(maze) - 1].index(' '), len(maze) - 1)


def find_path(maze, start):
    # finds the path from start to "!" within 20 moves or to the nearest "o"
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [[start]]
    seen = set(start)
    while queue:
        path = queue.pop(0)
        _x, _y = path[-1]
        if (_x, _y) == find_finish(maze):
            return path

        for d in direction:
            x, y = _x + d[0], _y + d[1]
            if 0 <= x < len(maze[0]) and 0 <= y < len(maze) and\
               maze[y][x] != '*' and (x, y) not in seen:
                queue.append(path + [(x, y)])
                seen.add((x, y))


f = open(sys.argv[1], 'r')
maze = f.read().split('\n')
f.close()

start = find_start(maze)
path = find_path(maze, start)
for y in range(len(maze)):
    for x in range(len(maze[y])):
        if (x, y) not in path and maze[y][x] == ' ':
            maze[y] = maze[y][:x] + '*' + maze[y][x+1:]
for i in maze:
    print(i)
