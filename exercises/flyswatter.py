#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
contents = contents[1:]
print contents
output = []
for case in range(1,num_cases+1):
    f, R, t, r, g = [float(a) for a in contents[0]]
    contents = contents[1:]
    print f, R, t, r, g
    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %.7f" % results)

write_output(output)


