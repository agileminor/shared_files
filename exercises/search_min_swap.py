#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input(False)
output = []
contents = contents[1:]
for case in range(1,num_cases+1):
#    print contents
    num_engine = int(contents[0])
    engine_list = contents[1:num_engine+1]
    num_query = int(contents[num_engine+1])
    query_list = contents[num_engine+2:num_engine+num_query+2]
    contents = contents[num_engine+num_query+2:]
#    print num_engine, engine_list
#    print num_query, query_list
    current_eng_list = engine_list[:]
    current_eng_dict = dict.fromkeys(engine_list,True)
    switch_count = 0
    for query in query_list:
        if query in current_eng_dict:
            current_eng_dict.pop(query, None)
        if len(current_eng_dict) == 0:
            switch_count += 1
            current_eng_dict = dict.fromkeys(engine_list,True)
            current_eng_dict.pop(query, None)
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % switch_count)

write_output(output)


