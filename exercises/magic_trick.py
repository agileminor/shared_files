#!/usr/bin/env python

import sys
read_file = sys.argv[1]
read_handle = open(read_file,'r')
contents = []
for line in read_handle:
    spline = line.split()
    contents.append(spline)
num_cases = int(contents[0][0])
contents = contents[1:]
results = []
grids = []
print contents
for i in range(num_cases):
    results.append((int(contents[i * 10][0]), int(contents[i*10+5][0])))
    grids.append([contents[i*10+1:i*10+5],contents[i*10+6:i*10+10]])
print results
print grids[0][0]
print grids[0][1]
output = []
for i in range(num_cases):
    first_row = grids[i][0][results[i][0]-1]
    second_row = grids[i][1][results[i][1]-1]
    print first_row
    print second_row
    item_count = 0
    for item in first_row:
        if item in second_row:
            item_count += 1
            found_item = item
    if item_count == 0:
        output.append("Case #" + str(i+1) + ": Volunteer cheated!")
    elif item_count == 1:
        output.append("Case #" + str(i+1) +": "+  str(found_item))
    else:
        output.append("Case #" + str(i+1) + ": Bad magician!")
print output
write_handle = open('magic.txt','w')
for item in output:
    write_handle.write(item)
    write_handle.write('\n')


