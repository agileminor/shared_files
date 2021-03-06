#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
for i in range(1,num_cases+1):
    counter = 2.0
    cum_time = 0.0
    C = float(contents[i][0])
    F = float(contents[i][1])
    X = float(contents[i][2])
    finish_time = X/counter
    farm_time = C/counter
    comp_time = X/counter
    comp_time = cum_time + finish_time
    cum_time += farm_time
    prev_comp_time = comp_time + 1
    while prev_comp_time > comp_time: 
        counter += F
        finish_time = X/counter
        farm_time = C/counter
        prev_comp_time = comp_time
        comp_time = cum_time + finish_time
        cum_time += farm_time
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(i) + ": %.7f" % prev_comp_time)

write_output(output)


