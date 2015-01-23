#!/usr/bin/env python

import sys, heapq
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
contents = contents[1:]
#print contents
for case in range(1,num_cases+1):
    x = [int(a) for a in contents[1]]
    neg_y = [-int(a) for a in contents[2]]
    contents = contents[3:]
    heapq.heapify(x)
    heapq.heapify(neg_y)
    total = 0
    while x != []:
        total += (heapq.heappop(x) * -heapq.heappop(neg_y))
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % total)

write_output(output)


