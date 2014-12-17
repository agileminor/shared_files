#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
contents = contents[1:]
output = []
for case in range(1,num_cases+1):
    results = 0.0
    N, K, B, T = int(contents[0][0]), int(contents[0][1]), int(contents[0][2]), int(contents[0][3])
    locations = [float(a) for a in contents[1]]
    speeds = [float(a) for a in contents[2]]
    contents = contents[3:]
#    print N, K, B, T
#    print locations
#    print speeds
    candidates = []
    blocks = {}
    chicks_count = 0
    swaps = 0
    i = N - 1
    delta = 1e-9
    while chicks_count < K and i > -1:
        location = locations[i]
        speed = speeds[i]
        if (B - location)/speed <= T:
#            print "adding ", i, " to chicks"
            temp_swap = 0
            found_block = False
            for block in blocks.keys():
#                print "checking", i, "versus", block
                collision_loc = ((locations[block] - location)/(speeds[block] - speed)) * speed
                for collision in blocks[block]:
                    if abs(collision - collision_loc) < delta: # add delta
                        found_block = True
                        break
                else:
                    blocks[block].append(collision_loc)
                    temp_swap += 1
            if not found_block:
                candidates.append(i)
                chicks_count += 1
                swaps += temp_swap
        else:
            blocks[i] = []
        i = i - 1
    if chicks_count < K:
        results = "IMPOSSIBLE"
    else:
        results = str(swaps)

    #for each calc if it can reach end in B, starting at right side
    #for each that can reach end in B, calc others that it will need to pass
    #for each other calc time of crossing (diff in locations / diff in speed)
    #check for conflicts with crossing time
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": " + results)

write_output(output)


