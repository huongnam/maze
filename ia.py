#!/usr/bin/env python
import sys
print("I AM IA\n\n")
print("OK\n\n")
maze = []


for i in range(len(maze)):
    line = sys.stdin.readline()
    maze.append(line)
print(''.join(maze))
