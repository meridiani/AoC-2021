import utils
import numpy as np
import sys

DATA = 'data/day05/realdata'

input = utils.load_string_data(DATA)

vent_coords = []
for line in input:
    vent_coords.append(list(map(int, line.replace(' -> ', ',').split(','))))

# find what the largest coordinate is and create a square grid containing only zeros
vent_map = np.zeros((np.max(vent_coords)+1, np.max(vent_coords)+1))

def mark_horizontal_vents(my_map, x1, x2, y):
    if x1 > x2:
        for x in range(x1, x2-1, -1):
            my_map[x][y] = vent_map[x][y] + 1
    elif x1 < x2:
        for x in range(x1, x2+1):
            my_map[x][y] = vent_map[x][y] + 1
    else:
        print('dunno')
    return my_map

def mark_vertical_vents(my_map, y1, y2, x):
    if y1 > y2:
        for y in range(y1, y2-1, -1):
            my_map[x][y] = vent_map[x][y] + 1
    elif y1 < y2:
        for y in range(y1, y2+1):
            my_map[x][y] = vent_map[x][y] + 1
    else:
        print('dunno')
    return my_map

for line in vent_coords:
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]

    if x1 == x2:
        vent_map = mark_vertical_vents(vent_map,y1,y2,x1)

    elif y1 == y2:
        vent_map = mark_horizontal_vents(vent_map,x1,x2,y1)
    else:
        incrementX = 1
        incrementY = 1
        if x1 > x2:
            incrementX = -1
        if y1 > y2:
            incrementY = -1

        x = x1
        y = y1

        vent_map[x][y] = vent_map[x][y] + 1

        while x != x2:
            x = x + incrementX
            y = y + incrementY
            vent_map[x][y] = vent_map[x][y] + 1

print((vent_map>= 2).sum())

#print('The first answer is:', 'something')
#print('The second answer is:', 'something')

#######################################################################
print('OK to go!')
