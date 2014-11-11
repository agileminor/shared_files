#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
contents = contents[1:]
#print contents
for case in range(1,num_cases+1):
    num_segs = int(contents[0][0])
    segs = [[int(a[0]), int(a[1])] for a in contents[1:num_segs+1]]
    contents = contents[num_segs+1:]
#    print segs
    count = 0
    while segs != []:
        check_seg = segs.pop()
        for seg in segs:
            check1 = seg[0] - check_seg[0]
            check2 = seg[1] - check_seg[1]
            check = check1 * check2
            if check < 0:
                count += 1
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % count)

write_output(output)


