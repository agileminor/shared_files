#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
for i in range(1,num_cases+1):
    R = int(contents[i][0])
    C = int(contents[i][1])
    M = int(contents[i][2])
    full_grid = [['*'] * R] * C
    empty_cells = R*C-M-1
    if R == 1 or C == 1:

    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(i) + ": %.7f" % results)

write_output(output)


