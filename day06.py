import utils

#DATA = 'data/day06/testdata'
DATA = 'data/day06/realdata'

input = list(map(int, utils.load_string_data(DATA)[0].split(',')))

# check if the list contains a zero, if it does append an 8
# decrement all values by one
# if any values are zero they become six not one
# iterate over 80 days

def check_for_new_fish(my_list):
    old_fish = 0
    for x in range(len(my_list)):
        if my_list[x] == 0:
            old_fish = old_fish + 1
    return old_fish

def create_new_fish(my_list, new_fish):
    for x in range(new_fish):
        my_list.append(8)
    return my_list


def next_day(my_list):
    my_list = [x - 1 for x in my_list]
    return my_list

def reset_old_fish(my_list):
    for x in range(len(my_list)):
        if my_list[x] < 0:
             my_list[x]= 6
    return my_list

fish = input
for day in range(1,81):
    print('Day is:',day)
    baby_fish = check_for_new_fish(fish)
    fish = next_day(fish)
    fish = reset_old_fish(fish)
    fish = create_new_fish(fish, baby_fish)


print(len(fish))

#print('The first answer is:', 'something')
#print('The second answer is:', 'something')

#######################################################################
print('OK to go!')
