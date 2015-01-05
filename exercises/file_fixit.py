#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

class Node(object):
    def __init__(self,value):
        self.value = value
        self.children = {}

def insert_dir(dir, current_node):
    leafs = dir[0][1:].split("/")
    count = 0
    for leaf in leafs:
        if leaf in current_node.children:
            current_node = current_node.children[leaf]
        else:
            new_node = Node(leaf)
            current_node.children[leaf] = new_node
            current_node = new_node
            count += 1
            #print "inserting ", leaf
    return count


num_cases, contents = read_input()
contents = contents[1:]
#print contents
output = []
for case in range(1,num_cases+1):
    print case
    temp = contents[0]
    N, M = int(temp[0]),int(temp[1])
    #print N
    #print M
    #print contents
    contents = contents[1:]
    current_dirs = contents[:N]
    #print current_dirs
    future_dirs = contents[N:N+M]
    contents = contents[N+M:]
    dir_tree_root = Node(None)
    for dir in current_dirs:
        insert_dir(dir, dir_tree_root)
    count = 0
    for dir in future_dirs:
        count += insert_dir(dir, dir_tree_root)
    #    print count
    results = 0.0
    #    print i, finish_time, farm_time, prev_comp_time, comp_time, cum_time, counter
    output.append("Case #" + str(case) + ": %i" % count)

write_output(output)

