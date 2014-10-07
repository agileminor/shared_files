#!/usr/bin/env python

import sys
def read_input():
    read_file = sys.argv[1]
    read_handle = open(read_file,'r')
    contents = []
    for line in read_handle:
        spline = line.split()
        contents.append(spline)
    num_cases = int(contents[0][0])
    return num_cases, contents


def write_output(output):
    write_handle = open(sys.argv[2],'w')
    for item in output:
        write_handle.write(item)
        write_handle.write('\n')


