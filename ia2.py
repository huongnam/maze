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

def valid_move():



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

        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == name:
                    pos = (x, y)
                if maze[y][x] == "o":
                    coin.append((x, y))
                if maze[y][x] == "!":
                    special_coin.append((x, y))

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

        if special_coin != []:
            min_distance(pos, special_coin)
            move(pos, get_target(pos, special_coin))
        else:
            min_distance(pos, coin)
            move(pos, get_target(pos, coin))




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
