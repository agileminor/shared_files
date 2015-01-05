#!/usr/bin/env python
###
###
# still not working on small data set, but works on test case data
#
###

import sys
from code_jam_io import read_input
from code_jam_io import write_output
import heapq
import copy


def check_connection(start_city, flight_dict, visited_list, dead_list):# won't work because visited sites are already stripped out of linking sites
    # flight list should be a copy of main flight dict
    connected = False
#    print flight_dict
    visited_dict = {start_city:1, visited_list[-1]:1}
    for item in dead_list:
        visited_dict[item] = 1
    if flight_dict[start_city] == []:
        return connected
#    print "start = ", start_city, "visited_list = ", visited_list
    queue = copy.deepcopy(flight_dict[start_city])
    while queue != []:
        current_city = queue.pop()
        while current_city in visited_dict:
            if queue == []:
                break
            current_city = queue.pop()
        if current_city not in visited_dict:
            visited_dict[current_city] = 1
            if current_city in visited_list:
                return True
            else:
                queue += flight_dict[current_city]
#        print current_city, queue, visited_dict.keys()
    return False

num_cases, contents = read_input(False)
output = []
contents = contents[1:]
for case in range(1,num_cases+1):
    print "case", case
    N, M = contents[0].split()
    N = int(N)
    M = int(M)
    city_value = contents[1:N+1]
    city_value = map(int, city_value)
    city_heap = heapq.heapify(city_value[:])
    flights = contents[N+1:N+M+1]
    contents = contents[N+M+1:]
    city_list = range(1,N+1)
    dead_list = {}
    city_value_dict = {n+1: int(city_value[n]) for n in range(N)}
    value_city_dict = {int(city_value[n]): n+1 for n in range(N)}
    flight_dict = {}
    for pair in flights:
        pair = pair.split()
        value1 = int(pair[0])
        value2 = int(pair[1])
        if value1 in flight_dict:
            if value2 not in flight_dict[value1]:
                flight_dict[value1].append(value2)
        else:
            flight_dict[value1] = [value2]
        if value2 in flight_dict:
            if value1 not in flight_dict[value2]:
                flight_dict[value2].append(value1)
        else:
            flight_dict[value2] = [value1]
                
    final_value = ""
    initial_flight_dict = copy.deepcopy(flight_dict)
    current_city_num = value_city_dict[min(city_value)]
    prev_min_list = [float("Inf")]
    prev_city_list = []
    #print flight_dict
    #print city_value_dict
    if M == 0:
        final_value = str(city_value_dict[1])
        city_list = []
    while city_list != []:
        solo_list = []
        min_list = []
        if current_city_num not in dead_list:
            city_list.remove(current_city_num)
            dead_list[current_city_num] = 1
            final_value += str(city_value_dict[current_city_num])
        #print "current = ", current_city_num
        for city in flight_dict[current_city_num]:
            #print city
            #print flight_dict
            if current_city_num in flight_dict[city]:
                flight_dict[city].remove(current_city_num)
            if city in city_list:
                if not check_connection(city, initial_flight_dict, prev_city_list[:] + [current_city_num], dead_list):
        #            print city, "not connected", dead_list.keys()
                    solo_list.append(city_value_dict[city])
                else:
        #            print city, "connected", dead_list.keys()
                    min_list.append(city_value_dict[city])
        #print solo_list
        #print min_list
        #print prev_min_list
        #print prev_city_list
        #print flight_dict
        #print city_list
        if solo_list == [] and min_list == []:
            current_city_num = prev_city_list.pop()
            prev_min_list.pop()

        elif solo_list != []:
            prev_city_list.append(current_city_num)
            if min_list != []:
                temp_min = min(min(solo_list), min(min_list))
            else:
                temp_min = min(solo_list)
            current_city_num = value_city_dict[temp_min]
            if temp_min in solo_list:
                solo_list.remove(city_value_dict[current_city_num])
            else:
                min_list.remove(city_value_dict[current_city_num])
            if solo_list == [] and min_list == []:
                prev_min_list.append(float("Inf"))
            elif solo_list == []:
                prev_min_list.append(min(min_list))
            elif min_list == []:
                prev_min_list.append(min(solo_list))
            else:
                prev_min_list.append(min(min(min_list),min(min_list)))

        else:
            prev_city_list.append(current_city_num)
            temp_min = min(min_list)
            if temp_min <= min(prev_min_list):
                current_city_num = value_city_dict[temp_min]
                min_list.remove(temp_min)
                if min_list == []:
                    prev_min_list.append(float("Inf"))
                else :
                    prev_min_list.append(min(min_list))
            else:
                prev_city_list.pop()
                current_city_num = prev_city_list.pop()
                prev_min_list.pop()
                #current_city_num = value_city_dict[min(prev_min_list)]
                #prev_min_list = prev_min_list[:prev_min_list.index(min(prev_min_list))]

    print final_value
                




    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": " + final_value)

write_output(output)


