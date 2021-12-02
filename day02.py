import utils

#DATA = 'data/day02/testdata'
DATA = 'data/day02/realdata'

# read in the list
# split each line into string space number
# start with [0,0]
# when string is forward x + number
# when string is down z + number
# when string is up z - number

sub_path = utils.load_string_data_split_on_space(DATA)

def calculate_position(data, i_x = 0, i_z = 0):
# Initialise coordinates to starting values
    x = i_x
    z = i_z

    for line in data:
        if line[0] == 'forward':
            x = x + int(line[1])
        elif line[0] == 'down':
            z = z + int(line[1])
        elif line[0] == 'up':
            z = z - int(line[1])
        else:
            print('Error, incorrect data:', line[0])

    return x, z

def calculate_position_and_aim(data, i_x = 0, i_z = 0, i_aim = 0):
# Initialise coordinates to starting values
    x   = i_x
    z   = i_z
    aim = i_aim

    for line in data:
        if line[0] == 'forward':
            x = x + int(line[1])
            z = z + (aim * int(line[1]))
        elif line[0] == 'down':
            aim = aim + int(line[1])
        elif line[0] == 'up':
            aim = aim - int(line[1])
        else:
            print('Error, incorrect data:', line[0])

    return x, z, aim

part1 = calculate_position(sub_path)
part2 = calculate_position_and_aim(sub_path)


print('The first answer is:', part1[0]*part1[1])
print('The second answer is:', part2[0]*part2[1])

#######################################################################
print('OK to go!')
