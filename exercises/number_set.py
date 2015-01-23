#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

primes = [2,[2]]
def sieve(max):
    primes = range(2,max+1)
    index = 0
    current = 2
    while current < max:
        inner_index = 2
        while current*inner_index <= max:
            if current * inner_index in primes:
                primes.remove(current*inner_index)
            inner_index += 1
        index += 1
        if index == len(primes):
            break
        current = primes[index]
    return primes


num_cases, contents = read_input()
output = []
contents = contents[1:]
print contents
for case in range(1,num_cases+1):
    A = int(contents[0][0])
    B = int(contents[0][1])
    P = int(contents[0][2])
    contents = contents[1:]
    print A, B, P
    print sieve(30)
    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %.7f" % results)

write_output(output)


