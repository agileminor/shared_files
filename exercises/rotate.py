#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

def check_array(new_array, check_R, check_B, array_len, row_len, K):
    found_R = False
    found_B = False
    for row in new_array:
        if row.find(check_R):
            found_R = True
        if row.find(check_B):
            found_B = True
        if found_R and found_B:
            return "Both"
    column_array = ["".join(a) for a in zip(*new_array)]
    for column in column_array:
        if column.find(check_R):
            found_R = True
        if column.find(check_B):
            found_B = True
        if found_R and found_B:
            return "Both"
    queue = [[(a,b), new_array[a][b]] for a in range(array_len) for b in range(row_len-K) if array[a][b] != "."]


num_cases, contents = read_input()
output = []
contents = contents[1:]
print contents
for case in range(1,num_cases+1):
    results = 0.0
    N, K = [int(a) for a in contents[0]]
    array = contents[1:N+1]
    contents = contents[N+1:]
    print N, K
    print array
    new_array = []
    array_len = len(array)
    row_len = len(array[0][0])
    check_R = "".join(["R"] * K)
    check_B = "".join(["B"] * K)
    print check_R, check_B
    for row in array:
        row = list(row[0])

        row = [a for a in row if a != "."]
        row = ["."] * (row_len - len(row)) + row
        row = "".join(row)
        new_array.append(row)
    print new_array
    sys.exit()
    result = check_array(new_array, check_R, check_B, array_len, row_len, K)
        
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %.7f" % results)

write_output(output)


