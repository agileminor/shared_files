#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output
from UnionFind import UnionFind
from sieve import sieve


def calc_prime_factor(x, primes, P):
    return {a for a in primes if (a <= x/2 or a == x) and x %a == 0 and a >= P}



num_cases, contents = read_input()
output = []
contents = contents[1:]
#print contents
for case in range(1,num_cases+1):
    A = int(contents[0][0])
    B = int(contents[0][1])
    P = int(contents[0][2])
    contents = contents[1:]
    interval = range(A, B + 1)
    #print A, B, P
    print "sieve for ", B-A
    primes = sieve(B - A)
    print "trimming primes"
    primes = [a for a in primes if a >= P]
    print "calculating factors"
    set_dict2 = {}
    for prime in primes:
        set_dict2[prime] = [a for a in interval if a % prime == 0]
    #primes_dict = {item: calc_prime_factor(item, primes, P) for item in range(A, B+1)}
    #print primes_dict
    print "creating UnionFind"
    set_list = UnionFind()
    for item in range(A, B+1):
        set_list.makeSet([item])
    #set_dict = {prime: [] for prime in primes}
    #print "creating sets"
    #for item in range(A,B+1):
    #    for prime in primes_dict[item]:
    #        set_dict[prime].append(item)
    #print set_dict
    #print set_list.getNumGroups()
    print "reducing sets"
    for item in set_dict2:
        temp_list = set_dict2[item]
        if len(temp_list) > 1:
            for new_item in temp_list:
                set_list.union(temp_list[0],new_item)
    results = set_list.getNumGroups()
    #print results
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % results)

write_output(output)


