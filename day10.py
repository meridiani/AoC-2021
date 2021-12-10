import utils
import sys

DATA = 'data/day10/realdata'
#DATA = 'data/day10/testdata'

input = utils.load_string_data(DATA)

brackets = ['()', '{}', '[]', '<>']

syntax_points     = {')' : 3, ']' : 57, '}' : 1197, '>' : 25137, }
completion_points = {')' : 1, ']' : 2,  '}' : 3,    '>' : 4, }

def find_corrupted_logs(brackets, my_string):
    nav_log = my_string
    x       = len(nav_log)
    while x > 0:
        for bracket in brackets:
            nav_log = nav_log.replace(bracket,"")
        x = x - 1
    return nav_log

def remove_bras(my_string):
    nav_log = my_string
    bras = ['(', '[', '{', '<']
    for bra in bras:
        nav_log = nav_log.replace(bra, "")
    return nav_log

def swap_bras_for_kets(my_string):
    log = my_string.replace('(',')').replace('[',']').replace('{','}').replace('<','>')
    return log

def close_brackets(my_string):
    return my_string[::-1]

incomplete_logs = []
corrupted_logs  = []  
for line in input:
    log = find_corrupted_logs(brackets, line)
    corrupt_log = remove_bras(log)
    if len(corrupt_log) > 0:
        corrupted_logs.append(corrupt_log[0])
    else:
        incomplete_logs.append(log)

part1 = 0
for line in corrupted_logs:
    part1 = part1 + syntax_points.get(line)

scores = []
for line in incomplete_logs:
    completion = swap_bras_for_kets(close_brackets(line))
    score = 0
    for char in completion:
        score = 5*score
        score = score + completion_points.get(char)
    scores.append(score)

part2 = sorted(scores)[int(len(scores)/2)]
#######################################################################
print('The first answer is:', part1 )
print('The second answer is:', part2)
#######################################################################
print('OK to go!')
