#!/usr/bin/env python

import sys
read_file = sys.argv[1]
read_handle = open(read_file,'r')
contents = []
for line in read_handle:
    spline = line.split()
    contents.append(spline)
num_cases = int(contents[0][0])
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

write_handle = open(sys.argv[2],'w')
for item in output:
    write_handle.write(item)
    write_handle.write('\n')


