#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input(False)
print contents
output = []
target_string = "welcome to code jam"
target_len = len(target_string)
output_array_blank = [0] * len(target_string)
for case in range(1,num_cases+1):
    check_string = contents[case]
    check_len = len(check_string)
    output_array = [output_array_blank[:] for _ in range(check_len)]
    for i in range(check_len):
        output_array[i][0] = check_string[:i+1].count(target_string[:1])
    for i in range(1, check_len):
        for j in range(1,target_len):
            if check_string[i] != target_string[j]:
                output_array[i][j] = output_array[i-1][j]
            else:
                output_array[i][j] = output_array[i-1][j] + output_array[i-1][j-1]
        
    print output_array[check_len-1][target_len-1]

    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(i) + ": %.7f" % results)

write_output(output)


