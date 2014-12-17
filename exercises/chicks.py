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
    locations = [int(a) for a in contents[1]]
    speeds = [int(a) for a in contents[2]]
    contents = contents[3:]
    print N, K, B, T
    print locations
    print speeds
    #for each calc if it can reach end in B
    #for each that can reach end in B, calc others that it will need to pass
    #for each other calc time of crossing (diff in locations / diff in speed)
    #check for conflicts with crossing time
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %.7f" % results)

write_output(output)


