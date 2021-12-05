import utils
from numpy import *
import sys

DATA = 'data/day04/realdata'

with open(DATA) as f_in:
    lines = (line.rstrip() for line in f_in)
    lines = list((line for line in lines if line))

input = asarray(lines)

call_list = list(map(int, input[0].split(',')))

cards = []
for l in input[1:]:
    l = list(map(int, l.split()))
    cards.append(l)

cards = asarray(cards)

x = cards.reshape((100,5,5))
print(shape(x))

# I will be given on list of numbers followed by some 5,5 arrays
# for each number in the first list I need to check if the number is in the array
# if the number is in the array I need to mark it
# I could make the original array value zero and the new array one
# then I need to look for bingos in the one array
# if I have a bingo I need to know the number it did it for
# and the sum of what remains in the array

#call_list = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]

#x = array([
#    [[22, 13, 17, 11,  0],
#     [ 8,  2, 23,  4, 24],
#     [21,  9, 14, 16,  7],
#     [ 6, 10,  3, 18,  5],
#     [ 1, 12, 20, 15, 19]],
#    [[ 3, 15,  0,  2, 22],
#     [ 9, 18, 13, 17,  5],
#     [19,  8,  7, 25, 23],
#     [20, 11, 10, 24,  4],
#     [14, 21, 16, 12,  6]],
#    [[14, 21, 17, 24,  4],
#     [10, 16, 15,  9, 19],
#     [18,  8, 23, 26, 20],
#     [22, 11, 13,  6,  5],
#     [ 2,  0, 12,  3,  7]]])
#
mark_x = zeros_like(x)

def is_any_row_bingo(my_array):
    bingo = False
    t = my_array.sum(axis=0)
    if len(my_array) in t:
        bingo = True

    return bingo

def is_any_col_bingo(my_array):
    bingo = False
    t = my_array.sum(axis=1)
    if len(my_array) in t:
        bingo = True

    return bingo

# iterate over bingo numbers
bingo = False
for n in call_list:
    # iterate over cards
    for i in range(len(x)):
        for j in range(len(x[i])):
            for k in range(len(x[i])):
                if x[i][j][k] == n:
                    mark_x[i][j][k] = 1
                    x[i][j][k]      = 0
        if is_any_row_bingo(mark_x[i]) or is_any_col_bingo(mark_x[i]):
            bingo = True
    if bingo:
        break

answer = n*sum(x[i])
print(answer)
       
#print(n,i,j,k)


#print('answer is', n*sum(x))

#print('The first answer is:', 'something')
#print('The second answer is:', 'something')

#######################################################################
print('OK to go!')
