#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input(False)
print contents
output = []
target_string = "welcome to code jam"
for i in range(1,num_cases+1):
    check_string = contents[i]
    output_array = [0] * len(target_string)
    for letter in check_string:
        count = 0
        for check_letter in target_string:
            if count > 0 and output_array[count-1] == 0:
                break
            #print letter, check_letter
            if letter == check_letter:
                if count == 0:
                    output_array[count] += 1
                elif output_array[count] < output_array[count-1]:
                    output_array[count] += 1
            count += 1

    print output_array[-1]

    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(i) + ": %.7f" % results)

write_output(output)


