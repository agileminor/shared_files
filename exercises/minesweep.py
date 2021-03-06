#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

num_cases, contents = read_input()
output = []
for case in range(1,num_cases+1):
    R = int(contents[case][0])
    C = int(contents[case][1])
    M = int(contents[case][2])
    full_grid = []
    temp = []
    for i in range(R):
        temp = []
        for j in range(C):
            temp.append("*")
        full_grid.append(temp)
    empty_cells = R*C-M-1
    #print "empty_cells = ", empty_cells
    full_grid[0][0] = 'c'
    if empty_cells == 0:
        output.append("Case #" + str(case) + ":")
        for i in range(R):
            output.append("".join(full_grid[i]))
    elif R == 1:
        count = 1
        while empty_cells > 0:
            full_grid[0][count] = "."
            count += 1
            empty_cells -= 1
        output.append("Case #" + str(case) + ":")
        for i in range(R):
            output.append("".join(full_grid[i]))
    elif C == 1:
        count = 1
        while empty_cells > 0:
            full_grid[count][0] = "."
            count += 1
            empty_cells -= 1
        output.append("Case #" + str(case) + ":")
        for i in range(R):
            output.append("".join(full_grid[i]))
    elif C == 2:
        if empty_cells % 2 == 0:
            output.append("Case #" + str(case) + ":")
            output.append("Impossible")
        elif empty_cells < 3:
            output.append("Case #" + str(case) + ": Impossible")
        else:
            temp = (empty_cells + 1) / 2
            full_grid[0][1] = "."
            for i in range(1,temp):
                full_grid[i][0] = "."
                full_grid[i][1] = "."
            output.append("Case #" + str(case) + ":")
            for i in range(R):
                output.append("".join(full_grid[i]))
    elif empty_cells <= C * 2 - 1: # need to add fixes for R > 2
        if empty_cells % 2 == 0:
            output.append("Case #" + str(case) + ": Impossible")
        elif empty_cells < 3:
            output.append("Case #" + str(case) + ": Impossible")
        else:
            temp = (empty_cells + 1) / 2
            full_grid[1][0] = "."
            for i in range(1,temp):
                full_grid[0][i] = "."
                full_grid[1][i] = "."
            output.append("Case #" + str(case) + ":")
            for i in range(R):
                output.append("".join(full_grid[i]))
    else:
        temp = C
        full_grid[1][0] = "."
        for i in range(1,temp):
            full_grid[0][i] = "."
            full_grid[1][i] = "."
        empty_cells = empty_cells - (C*2-1)
        row_count = 2
        while empty_cells > 0:
            if empty_cells > C + 1:
                temp_row = ["."] * C
                full_grid[row_count] = temp_row
                row_count += 1
                empty_cells -= C
            elif empty_cells == C + 1:
                for i in range(C-1):
                    full_grid[row_count][i] = "."
                row_count += 1
                full_grid[row_count][0] == "."
                full_grid[row_count][1] == "."
                empty_cells = 0
            else:
                for i in range(empty_cells):
                    full_grid[row_count][i] = "."
                empty_cells = 0
        output.append("Case #" + str(case) + ":")
        for i in range(R):
            output.append("".join(full_grid[i]))
write_output(output)


