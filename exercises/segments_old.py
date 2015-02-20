#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
contents = contents[1:]
output = []
blanks = {9:[4],8:[],7:[3,4,5,6],6:[1],5:[1,4],4:[0,3,4],3:[4,5],2:[2,5],1:[0,3,4,5,6],0:[6]}
lits = {9:[0,1,2,3,5,6],8:[0,1,2,3,4,5,6],7:[0,1,2],6:[0,2,3,4,5,6],5:[0,2,3,5,6],4:[1,2,5,6],3:[0,1,2,3,6],2:[0,1,3,4,6],1:[1,2],0:[0,1,2,3,4,5]}
seg_dic = {9:"1111011",8:"1111111",7:"1110000",6:"1011111",5:"1011011",4:"0110011",3:"1111001",2:"1101101",1:"0110000",0:"1111110"}
#print num_cases, contents
for case in range(1,num_cases+1):
    segments = contents[case - 1][1:]
    print segments
    valid = [0,1,2,3,4,5,6,7,8,9] 
    broken = {0:[], 1:[],2:[],3:[],4:[],5:[],6:[]}
    seg_count = 0
    for segment in segments:
        # add index to point to broken check?
        print "valid =", valid
        lit = [a for a in range(7) if segment[a] == "1"]
        print lit
        remove_list = []
        for check_valid in valid:
            for one in lit:
                if one in blanks[check_valid] :
                    print "removing", check_valid, one
                    remove_list.append(check_valid)
                    break
                if  one in broken[(check_valid+seg_count)%10]:# need to think about whether this works or needs to be decremented?
                    print "removing", check_valid, one
                    remove_list.append(check_valid)
                    break
#
                
        for value in remove_list:
            valid.remove(value)
        for temp_index in range(len(valid)):
            for one_check in lits[valid[temp_index]]:
                if segment[one_check] == '0':
                    if one_check not in broken[(temp_index+seg_count)%10]: # ERRORS on this line
                        broken[(temp_index+seg_count)%10].append(one_check)

        seg_count += 1
        valid = [(a-1)%10 for a in valid]
    if len(valid) == 1:
        next = valid[0]
        bin_final = seg_dic[valid[0]]
        index = len(segments)-1
        xor_value = 0
        while index >= 0:
            next = (next + 1) % 10
            temp = int(seg_dic[next],2) ^ int(segments[index],2)
            xor_value = xor_value | temp
            index -= 1
#        print seg_dic[valid[0]], xor_value
        result = bin(int(seg_dic[valid[0]],2) & ~xor_value & 0b1111111111)[2:].zfill(7)
        # bin(result).zfill(7)
    else:
        result = "ERROR!" # need to add figuring out broken segment

    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %s" % result)

write_output(output)


