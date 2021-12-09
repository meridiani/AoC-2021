import utils
import sys

DATA = 'data/day09/realdata'
#DATA = 'data/day09/testdata'

input = utils.load_string_data(DATA)

heightmap = [] 
for i in range(len(input)):
    heightmap.append(list(map(int, list(input[i]))))

max_x = len(heightmap[0])
max_y = len(heightmap)

# for each number in the grid create a list of the number and the numbers around it
# if the number is not equal to any of the other numbers
# AND the number is the lowest number in the list
# the number is a low point so add to the low point list
# at the end sum the low_points and add the length of the list to find the sum of the risk levels
# the corners and sides are calculated separately as they are surrounded by less than four numbers

def check_loc_for_low_point(low_list, my_list):
    if check_loc_is_unique(my_list) and check_loc_is_min(my_list):
        low_list.append(my_list[0])
    return low_list

def check_loc_is_unique(my_list):
    if my_list.count(my_list[0]) == 1:
        return True
    return False

def check_loc_is_min(my_list):
    if my_list[0] == min(my_list):
        return True
    return False

low_points = []
for x in range(max_x):
    for y in range(max_y):
        loc      = heightmap[y][x]
        loc_list = []
        # find corners:
        if x == 0 and y == 0:
            # top left
            loc_list = [loc, heightmap[y+1][x], heightmap[y][x+1]]
            check_loc_for_low_point(low_points, loc_list)
        elif x == 0 and y == max_y - 1:
            # bottom left
            loc_list = [loc, heightmap[y-1][x], heightmap[y][x+1]]
            check_loc_for_low_point(low_points, loc_list)
        elif x == max_x - 1 and y == 0:
            # top right
            loc_list = [loc, heightmap[y][x-1], heightmap[y+1][x]]
            check_loc_for_low_point(low_points, loc_list)
        elif x == max_x - 1 and y == max_y - 1:
            # bottom right
            loc_list = [loc, heightmap[y-1][x], heightmap[y][x-1]]
            check_loc_for_low_point(low_points, loc_list)
        # now find edges
        elif x == 0:
            # left
            loc_list = [loc, heightmap[y-1][x], heightmap[y+1][x], heightmap[y][x+1]]
            check_loc_for_low_point(low_points, loc_list)
        elif x == max_x -1:
            # right
            loc_list = [loc, heightmap[y-1][x], heightmap[y+1][x], heightmap[y][x-1]]
            check_loc_for_low_point(low_points, loc_list)
        elif y == 0:
            # top
            loc_list = [loc, heightmap[y][x-1], heightmap[y+1][x], heightmap[y][x+1]]
            check_loc_for_low_point(low_points, loc_list)
        elif y == max_y -1:
            # bottom
            loc_list = [loc, heightmap[y][x-1], heightmap[y-1][x], heightmap[y][x+1]]
            check_loc_for_low_point(low_points, loc_list)
        else:
            # must be in the middle
            loc_list = [loc, heightmap[y-1][x], heightmap[y][x+1], heightmap[y+1][x], heightmap[y][x-1]]
            check_loc_for_low_point(low_points, loc_list)

#######################################################################
print('The first answer is:', (sum(low_points) + len(low_points)))
print('The second answer is:', 'something')
#######################################################################
print('OK to go!')
