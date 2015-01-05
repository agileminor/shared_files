#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
contents = contents[1:]
output = []
blanks = {9:[4],8:[],7:[3,4,5,6],6:[1],5:[1,4],4:[0,3,4],3:[4,5],2:[2,5],1:[0,3,4,5,6],0:[6]}
seg_dic = {9:"1111011",8:"1111111",7:"1110000",6:"1011111",5:"1011011",4:"0110011",3:"1111001",2:"1101101",1:"0110000",0:"1111110"}
print num_cases, contents
for case in range(1,num_cases+1):
    segments = contents[case - 1][1:]
    print segments
    valid = [0,1,2,3,4,5,6,7,8,9]
    for segment in segments:
        lit = [a for a in range(7) if segment[a] == "1"]
        print lit
        for check_valid in valid:
            for one in lit:
                if one in blanks[check_valid]:
                    valid.remove(check_valid)
                    break
        valid = [(a+1)%7 for a in valid]
    if len(valid) == 1:
        result = seg_dic[valid[0]]
    else:
        result = "ERROR!"

    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %s" % result)

write_output(output)


