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

while True:
    s = sys.stdin.readline()
    if 'HELLO' in s:
        sys.stdout.write('I AM NAM\n\n')
    if 'YOU ARE' in s:
        sys.stdout.write('OK\n\n')
    if 'MAZE' in s:
        l = []
        while len(s) > 0:
            s = input()
            f = open('getmaze', 'w')
            f.write(s + "\n")
            f.close()
        sys.stdout.write('MOVE UP\n\n')
        # f = open('getmaze', 'r')
        # line = f.readline()
        # while line:
        #     l.append(line)
        #     line = f.readline()
        # f.close()
