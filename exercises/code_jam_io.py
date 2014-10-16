#!/usr/bin/env python

import sys
def read_input(strip=True):
    read_file = sys.argv[1]
    read_handle = open(read_file,'r')
    contents = []
    for line in read_handle:
        if strip:
            spline = line.split()
            contents.append(spline)
        else:
            contents.append(line.strip())
    if strip:
        num_cases = int(contents[0][0])
    else:
        num_cases = int(contents[0])
    return num_cases, contents


def write_output(output):
    write_handle = open(sys.argv[2],'w')
    for item in output:
        write_handle.write(item)
        write_handle.write('\n')


