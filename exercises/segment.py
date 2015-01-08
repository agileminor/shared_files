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
#    print segments
    valid = [0,1,2,3,4,5,6,7,8,9] 
    seg_count = 0
    result_list = []
    for check_valid in valid:
#        print "checking", check_valid
        broken = []
        terminate_segments = False
        current_check = check_valid
        for segment in segments:
#            print "segment", segment
            if terminate_segments:
                break
            lit = [a for a in range(7) if segment[a] == "1"]
            for one in lit:
                if one in blanks[current_check]:
                    terminate_segments = True
            for one in lits[current_check]:
                if segment[one] == "1":
                    if one in broken:
                        terminate_segments = True
                else:
                    if one in broken:
                        pass
                    else:
                        broken.append(one)
            current_check = (current_check - 1) % 10
        else:
            if terminate_segments == False:
#                print "adding", current_check
                result_list.append((current_check, broken))

    if len(result_list) == 1:
#        print broken

        result = seg_dic[result_list[0][0]]
        for broken_seg in result_list[0][1]:
            result = result[:broken_seg] + "0" + result[broken_seg + 1:]
    else:
        result = "ERROR!" # need to add figuring out broken segment

    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %s" % result)

write_output(output)


