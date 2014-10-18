#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output
def create_flip(str1, str2):
#    print "strings = ", str1, str2
    output = []
    for i in range(len(str1)):
        if str1[i] == str2[i]:
            output.append('0')
        else:
            output.append('1')
    return "".join(output)
num_cases, contents = read_input()
output = []
for case in range(1,num_cases+1):
    N = contents[1+(case-1)*3][0]
    L = contents[1+(case-1)*3][1]
    plugs = contents[2+(case-1)*3]
    plugs_dict = {a:a for a in plugs}
    devices = contents[3+(case-1)*3]
    devices_dict = {a:a for a in devices}
    device = devices[0]
    flips = []
    for plug in plugs:
        flips.append(create_flip(device, plug))
    min_count = int(L) + 1
    min_flip = "NOT POSSIBLE"
    for flip in flips:
        for plug in plugs:
            if create_flip(flip, plug) not in devices_dict:
                break
        else:
            current_count = sum([1 for a in flip if a == "1"]) 
            if current_count < min_count:
                min_flip = flip
                min_count = current_count
        
    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    if min_flip == "NOT POSSIBLE":
        output.append("Case #" + str(case) + ": " + min_flip)
    else:
        output.append("Case #" + str(case) + ": %i" % min_count)

write_output(output)


