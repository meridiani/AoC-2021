import utils

#DATA = 'data/day07/testdata'
DATA = 'data/day07/realdata'

input = utils.load_string_data(DATA)

crabs = list(map(int,input[0].split(',')))

max_crab = max(crabs)

fuel_consumption = []
for x in range(max_crab + 1):
    fuel_used = sum([abs(y - x) for y in crabs])
    fuel_consumption.append(fuel_used)

def triangular_numbers(n):
    i, t = 1, 0
    while i <= n:
        yield t
        t += i
        i += 1


triangle_fuel_list = list(triangular_numbers(max_crab+1))

fuel_consumption_2 = []
for x in range(max_crab + 1):
    fuel_used = sum([triangle_fuel_list[abs(y - x)] for y in crabs])
    fuel_consumption_2.append(fuel_used)


print('The first answer is:', min(fuel_consumption))
print('The second answer is:', min(fuel_consumption_2))

#######################################################################
print('OK to go!')
