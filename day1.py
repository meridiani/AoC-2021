#!/usr/bin/env python3
import sys

### open file

try:
#    f = open('test1.txt','r')
    f = open('realdata.txt','r')
except FileNotFoundError as err:
    print(f"Maria! There is an Error: {err}")
else:    
    l = [int(line) for line in f]
    
    count = 0
    for x in range(1,len(l)):
        if l[x] > l[x-1]:
            count = count + 1 

# starting at the second element
# compare the element to the one before
# the the element is higher it is an increase
# stop at the last element


    f.close()

print('The answer is:', count)

#######################################################################
print('OK to go!')

