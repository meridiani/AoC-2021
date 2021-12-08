import utils
import sys

DATA = 'data/day08/realdata'
#DATA = 'data/day08/testdata'

#######################################################################
### Load data
input = utils.load_string_data(DATA)

signal_patterns = []
output_values = []

for line in input:
    x = line.split('|')
    signal_patterns.append(x[0].split())
    output_values.append(x[1].split())
#######################################################################
### Part 1: find 1, 4, 7 & 8
part1 = 0
for line in output_values:
    for number in range(len(line)):
        x = len(line[number])
        if x == 2 or x == 3 or x == 4 or x == 7:
            part1 = part1 + 1
#######################################################################
### Part 2:
# b e f are unique
# 1 -> len(x) == 2, cf ------> len(x) = 1
# 4 -> len(x) == 4, bcdf  ---> len(x) = 4
# 7 -> len(x) == 3, acf -----> len(x) = 3
# 8 -> len(x) == 7, abcdefg -> len(x) = 7

# 2 -> len(x) == 5, acdeg ---> is 5 length and does not contain b or f
# 3 -> len(x) == 5, acdfg ---> is 5 length and contains only f not b
# 5 -> len(x) == 5, abdfg ---> is 5 length and contains b & f
# 9 -> len(x) == 6, abcdfg --> 6 length and is 8 - e
# 0 -> len(x) == 6, abcefg --> is 6 length and is not nine or six
# 6 -> len(x) == 6, abdefg --> is 6 lenght and is 5 + e
#
# a is in 0, 2, 3, 5, 6, 7, 8, 9;    F = 8; is not c
# b is in 0, 4, 5, 6, 8, 9;          F = 6; unique
# c is in 0, 1, 2, 3, 4, 7, 8, 9;    F = 8; is in all 1, 4, 7, 8
# d is in 2, 3, 4, 5, 6, 8, 9;       F = 7; is not g
# e is in 0, 2, 6, 8;                F = 4; unique
# f is in 0, 1, 3, 4, 5, 6, 7, 8, 9; F = 9; unique
# g is in 0, 2, 3, 5, 6, 8, 9;       F = 7; is in 8 but not 1, 4, 7

# line is a list, number is an item in the list
def assign_known_numbers(number_list):
    known_numbers = {}
    for number in number_list:
        if len(number) == 2:
            known_numbers['1'] = number
        elif len(number) == 4:
            known_numbers['4'] = number
        elif len(number) == 3:
            known_numbers['7'] = number
        elif len(number) == 7:
            known_numbers['8'] = number
        else:
            continue
    return known_numbers

def alphabetically_sort_strings_in_list(my_list):
    for x in range(len(my_list)):
        my_list[x] = "".join(sorted(my_list[x]))
    return my_list

def find_b_e_f(my_line):
    primer = {}
    for char in 'abcdefg':
        f_char = sum(char in x for x in my_line)
        if f_char == 6:
            primer['b'] = char
        elif f_char == 4:
            primer['e'] = char
        elif f_char == 9:
            primer['f'] = char
    return primer

def assign_235(known_numbers, number_list, primer):
# 2 -> len(x) == 5, acdeg ---> is 5 length and does not contain b or f
# 3 -> len(x) == 5, acdfg ---> is 5 length and contains only f not b
# 5 -> len(x) == 5, abdfg ---> is 5 length and contains b & f
    for number in number_list:
        if len(number) == 5: # must be two, three or five
            if primer['b'] not in number and primer['f'] not in number:
                known_numbers['2'] = number
            elif primer['f'] in number and primer['b'] not in number:
                known_numbers['3'] = number
            elif primer['b']in number and primer['f'] in number:
                known_numbers['5'] = number
            else:
                print('fishy')
                known_numbers['fishy'] = True
        else:
            continue
    return known_numbers

def assign_609(known_numbers, number_list, primer):
# 9 -> len(x) == 6, abcdfg --> 6 length and is 8 - e
# 0 -> len(x) == 6, abcefg --> is 6 length and is not nine or six
# 6 -> len(x) == 6, abdefg --> is 6 lenght and is 5 + e
    six = "".join(sorted(known_numbers['5']+primer['e']))
    for number in number_list:
        if len(number) == 6:
            if known_numbers['8'].replace(primer['e'],'') == number:
                known_numbers['9'] = number
            elif number == six:
                known_numbers['6'] = number 
            else:
                known_numbers['0'] = number
        else:
            continue
    return known_numbers

number_dicts = []
for line in signal_patterns:
    line = alphabetically_sort_strings_in_list(line)
    known_numbers = assign_known_numbers(line)

    primer = find_b_e_f(line)

    assign_235(known_numbers, line, primer)
    assign_609(known_numbers, line, primer)

    number_dicts.append(known_numbers)

# at this point we know all thenumber so we need to start reading through the output values
total = 0
for x in range(len(output_values)):
    output  = alphabetically_sort_strings_in_list(output_values[x])
    numbers = {v: k for k, v in number_dicts[x].items()}
    # maria
    entry = ''
    for i in output:
        entry = entry + numbers.get(i)
    total = total + int(entry)
#######################################################################
print('The first answer is:', part1)
print('The second answer is:', total)
#######################################################################
print('OK to go!')
