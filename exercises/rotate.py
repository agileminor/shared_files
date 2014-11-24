#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

def print_array(array):
    for item in array:
        print item


def check_array(new_array, check_R, check_B, array_len, row_len, K):
    found_R = False
    found_B = False
    for row in new_array:
        if row.find(check_R) > -1:
            found_R = True
        if row.find(check_B) > -1:
            found_B = True
        if found_R and found_B:
            return "Both"
    column_array = ["".join(a) for a in zip(*new_array)]
    for column in column_array:
        if column.find(check_R) > -1:
            found_R = True
        if column.find(check_B) > -1:
            found_B = True
        if found_R and found_B:
            return "Both"
    queue = [[(a,b), new_array[a][b], 0] for a in range(array_len) for b in range(row_len - K + 1) if new_array[a][b] != "."]# need to change to row_len-k+1
    while queue != []:
        current_element = queue[0]
        queue = queue[1:]
        loc = current_element[0]
        value = current_element[1]
        if current_element[2] == 0:
            moves = [-1,1]
        else:
            moves = [current_element[2]]
        for move in moves:
            new_loc = (loc[0] + move,loc[1] + 1)
            if new_loc[0] >= 0 and new_loc[0] < array_len and new_loc[1] >= 0 and new_loc[1] < row_len:
                new_value = new_array[new_loc[0]][new_loc[1]]
                if new_value == value[0]:
                    new_value = value+new_value
                    if new_value == check_R:
                        found_R = True
                    elif new_value == check_B:
                        found_B = True
                    else:
                        queue.append([new_loc,new_value, move])
        if found_R and found_B:
            return "Both"
    if found_R:
        return "Red"
    elif found_B:
        return "Blue"
    else:
        return "Neither"


num_cases, contents = read_input()
output = []
contents = contents[1:]
#print contents
for case in range(1,num_cases+1):
    results = 0.0
    N, K = [int(a) for a in contents[0]]
    array = contents[1:N+1]
    contents = contents[N+1:]
    #print N, K
    #print_array(array)
    new_array = []
    array_len = len(array)
    row_len = len(array[0][0])
    check_R = "".join(["R"] * K)
    check_B = "".join(["B"] * K)
    #print check_R, check_B
    for row in array:
        row = list(row[0])

        row = [a for a in row if a != "."]
        row = ["."] * (row_len - len(row)) + row
        row = "".join(row)
        new_array.append(row)
    #print_array(new_array)
    result = check_array(new_array, check_R, check_B, array_len, row_len, K)
    #print result
        
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": " + result)

write_output(output)


