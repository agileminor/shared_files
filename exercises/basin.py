#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output
max_value = 10001
moves = [[-1,0,"N"],[0,-1,"W",],[0,1,"E",],[1,0,"S"]]
def gen_letter():
    for letter in range(97,97+26):
        yield chr(letter)
def find_sink(table,output_table, row_index, column_index, letter_index):
    #print "in sink", row_index, column_index
    #print table
    #print output_table
    if output_table[row_index][column_index]:
        #print "found previous value"
        return output_table[row_index][column_index]
    result= []
    for move in moves:
        possible_move = [move[0] + row_index, move[1] + column_index]
        if min(possible_move) < 0 or possible_move[0] > len(table)-1 or possible_move[1] > len(table[0])-1:
            result.append(max_value)
            continue
        else:
            result.append(int(table[possible_move[0]][possible_move[1]]))
    #print result, min(result), table[row_index][column_index]
    if min(result) >= int(table[row_index][column_index]):
        #print "found sink"
        new_output = letter_index.next()
        output_table[row_index][column_index] = new_output
        return new_output
    else:
        #print "not in a sink, moving on"
        current_min = max_value
        min_move = []
        for i in range(len(moves)):
            if result[i] < current_min:
                min_move = moves[i]
                current_min = result[i]
        sink =  find_sink(table, output_table, row_index + min_move[0], column_index + min_move[1], letter_index)
        output_table[row_index][column_index] = sink
        return sink

num_cases, contents = read_input()
table_line = False
tables = []
output_tables = []
for line in contents[1:]:
    if not table_line:
        H = int(line[0])
        W = int(line[1])
        table=[]
        count = 0
        table_line = True
    else:
        table.append(line)
        count += 1
        if count == H:
            table_line = False
            tables.append(table)
for table in tables:
    letter_index = gen_letter()
    letter = ["a"]
    H = len(table)
    W = len(table[0])
    #print "table = ", H, W
    output_table = [[None for a in range(W)] for b in range(H)]
    for row_index in range(H):
        for column_index in range(W):
            find_sink(table, output_table, row_index, column_index, letter_index)
    output_tables.append(output_table)
    print output_table
output = []
for i in range(1,num_cases+1):
    results = 0.0
        #print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(i) + ":")
    for line in output_tables[i-1]:
        output.append(" ".join(line))

write_output(output)


