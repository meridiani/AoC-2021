#!/usr/bin/env python
import utils

#DATA = 'data/day01/testdata'
DATA = 'data/day01/realdata'

# starting at the second element
# compare the element to the one before
# the the element is higher it is an increase
# stop at the last element
def find_total_increases(sonar_list):
    count = 0
    for x in range(1,len(sonar_list)):
        if sonar_list[x] > sonar_list[x-1]:
            count = count + 1 
    return count

def sum_three_elements(data):
    n = []
    for x in range(0,len(data)-2):
        y = data[x]+data[x+1]+data[x+2]
        n.append(y)
    return n

print('The first answer is:', find_total_increases(utils.load_data(DATA)))
print('The second answer is:', find_total_increases(sum_three_elements(utils.load_data(DATA))))

#######################################################################
print('OK to go!')
