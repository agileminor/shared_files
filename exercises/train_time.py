#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
contents = contents[1:]
#print contents
output = []
for case in range(1,num_cases+1):
    TAT = int(contents[0][0])
    NA = int(contents[1][0])
    NB = int(contents[1][1])
    A_trips = contents[2:2+NA]
    B_trips = contents[2+NA:2+NA+NB]
    #print TAT, NA, NB
    #print A_trips
    #print B_trips
    contents = contents[2+NA+NB:]
    a_arrival = []
    a_departure = []
    b_arrival = []
    b_departure = []
    for trip in A_trips:
        a_departure.append(round((float(trip[0][0:2]) + float(trip[0][3:])/60),5))
        b_arrival.append(round((float(trip[1][0:2]) + float(trip[1][3:])/60 + TAT/60.0),5))
    for trip in B_trips:
        b_departure.append(round((float(trip[0][0:2]) + float(trip[0][3:])/60),5))
        a_arrival.append(round((float(trip[1][0:2]) + float(trip[1][3:])/60 + TAT/60.0),5))
    #print a_arrival, a_departure
    #print b_arrival, b_departure
    needed_a = 0
    needed_b = 0
    for leaving_a in a_departure:
        earlier = [a for a in a_arrival if a <= leaving_a] # try without finding closest
        if len(earlier) > 0:
            earlier.sort()
            a_arrival.remove(earlier[-1])
        else:
            needed_a += 1
    for leaving_b in b_departure:
        earlier = [b for b in b_arrival if b <= leaving_b] # try without finding closest
        if len(earlier) > 0:
            earlier.sort()
            b_arrival.remove(earlier[-1])
        else:
            needed_b += 1
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i %i" % (needed_a, needed_b))
    #print output

write_output(output)


