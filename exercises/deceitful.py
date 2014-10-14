#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
for case in range(1,num_cases+1):
    num_blocks = int(contents[(case-1) * 3 + 1][0])
    #print num_blocks
    n_blocks = [float(x) for x in contents[(case-1) * 3 + 2]]
    k_blocks = [float(x) for x in contents[(case-1) * 3 + 3]]
    #print n_blocks
    #print k_blocks
    fixed_n_blocks = sorted(n_blocks)
    fixed_k_blocks = sorted(k_blocks)
#    print num_blocks, n_blocks, k_blocks
    # deceitful war
    dec_n_points = 0
    n_points = 0
    n_blocks = fixed_n_blocks[:]
    k_blocks = fixed_k_blocks[:]
    for x in range(num_blocks):
        n_block_min = n_blocks[0]
        n_block_max = n_blocks[-1]
        k_block_max = k_blocks[-1]
        k_block_min = k_blocks[0]
        if len(k_blocks) > 1:
            k_block_next = k_blocks[-2]
        else:
            k_block_next = 0
        if n_block_min < k_block_min:
            n_block_claim = k_block_max - (k_block_max - k_block_next)/2
            if n_block_claim < n_block_min:
                n_block_claim = k_block_max - (k_block_max - n_block_min)/2
            n_block = n_blocks[0]
            n_blocks = n_blocks[1:]
            k_block = k_blocks[-1]
            k_blocks = k_blocks[:-1]
        else: # n_block_min > k_block_min:
            n_block_claim = k_block_max + (1-k_block_max)/2
            n_block = n_blocks[0]
            n_blocks = n_blocks[1:]
            k_block = k_blocks[0]
            k_blocks = k_blocks[1:]
        print n_block, k_block
        if n_block > k_block:
            dec_n_points += 1
    # normal war
    n_blocks = fixed_n_blocks[:]
    k_blocks = fixed_k_blocks[:]
    for x in range(num_blocks):
        n_block = n_blocks[0]
        n_blocks = n_blocks[1:]
        if n_block > max(k_blocks):
            k_block = k_blocks[0]
            k_blocks = k_blocks[1:]
        else:
            for block in k_blocks:
                if block > n_block:
                    k_block = block
                    k_blocks.remove(block)
                    break
        if n_block > k_block:
            n_points += 1
    #print dec_n_points, n_points
    output.append("Case #" + str(case) + ": %i %i" % (dec_n_points, n_points))


    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    #output.append("Case #" + str(i) + ": %.7f" % results)
write_output(output)


