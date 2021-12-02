import utils

#DATA = 'data/day03/testdata'
DATA = 'data/day03/realdata'

report = utils.load_string_data(DATA)

# cleanse the data
#it = iter(report)
#bin_length = len(next(it))
#if not all(len(l) == bin_length for l in it):
#    raise ValueError('Error! Not all elements are the same length!')

def how_many_ones(datalist, position):
    ones = 0
    for line in datalist:
        ones = ones + int(line[position])
    return ones

def most_common_bit(datalist, position):
    x = how_many_ones(datalist, position)
    l = len(datalist)

    if x > l/2:
        mcb   = '1'
    elif x < l/2:
        mcb   = '0'
    elif x == l/2:
        mcb   = '1'
    else:
        mcb   = 'shrug'

    return mcb

def least_common_bit(datalist, position):
    x = how_many_ones(datalist, position)
    l = len(datalist)

    if x > l/2:
        lcb   = '0'
    elif x < l/2:
        lcb   = '1'
    elif x == l/2:
        lcb   = '0'
    else:
        lcb   = 'shrug'

    return lcb

def calculate_d_gamma(my_list):
    l       = len(my_list[0])
    d_gamma = ''

    for x in range(l):
        d_gamma = d_gamma + most_common_bit(my_list, x)

    return d_gamma

def calculate_d_epsilon(my_list):
    l         = len(my_list[0])
    d_epsilon = ''

    for x in range(l):
        d_epsilon = d_epsilon + least_common_bit(my_list, x)

    return d_epsilon

# iterating over d_gamma
# check if the first charctor of each item in the list is the same as gamma
# if it is add to the new list
# if not skip
# at the end recalculate d_gamma
# then do it again
# until the list is only one item long

initial_d_gamma   = calculate_d_gamma(report)
initial_d_epsilon = calculate_d_epsilon(report)
initial_list      = report
initial_position  = 0

def filter_list(my_list, position, bit):
    n = []
    for line in my_list:
        if line[position] == bit:
            n.append(line) 

    return n  

# given a list and a d_gamma
# filter the list and check if length is one
# if one return the list
# if not create new list and new g_gamma and start again

def find_oxygen_generator_rating(initial_list, initial_position):
    oxygen_generator_rating = initial_list
    position                = initial_position

    while len(oxygen_generator_rating) != 1:
        mcb = most_common_bit(oxygen_generator_rating, position)
        oxygen_generator_rating = filter_list(oxygen_generator_rating, position, mcb)
        position = position + 1

    return oxygen_generator_rating

def find_co2_scrubber_rating(initial_list, initial_position):
    co2_scrubber_rating = initial_list
    position            = initial_position

    while len(co2_scrubber_rating) != 1:
        lcb = least_common_bit(co2_scrubber_rating, position)
        co2_scrubber_rating = filter_list(co2_scrubber_rating, position, lcb)
        position = position + 1

    return co2_scrubber_rating

o2_rating  = find_oxygen_generator_rating(initial_list, initial_position)
co2_rating = find_co2_scrubber_rating(initial_list, initial_position)

print('The first answer is:', int(initial_d_gamma,2)*int(initial_d_epsilon,2))
print('The second answer is:', int(o2_rating[0],2)*int(co2_rating[0],2))

#######################################################################
print('OK to go!')
