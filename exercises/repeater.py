#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output
from collections import deque

num_cases, contents = read_input(False)
#print contents
contents = deque(contents[1:])
output = []
for case in range(1,num_cases+1):
    word_count = int(contents.popleft())
    words = []
    for i in range(word_count):
        words.append(contents.popleft())
    template = ""
    word_changes = []
    out_str = "Fegla Won"
    for word in words:
        last_char = ""
        short_word = []
        change_count = 0
        change = []
        for letter in word:
            if letter != last_char:
                short_word.append(letter)
                if last_char != "":
                    change.append(change_count)
                change_count = 0
            else:
                change_count += 1
            last_char = letter
        change.append(change_count)
#        print short_word
        if template == "":
            template = "".join(short_word)
        else:
            if template != "".join(short_word):
                not_possible = True
                break
#        print change
        word_changes.append(change)
    else:
#        print word_changes
        zipped_word_changes = zip(*word_changes)
#        print zip(*word_changes)
        min_total = 0
        for temp_set in zipped_word_changes:
            min_set = float("Inf")
            for i in range(len(word_changes)):
                total = 0
                for value in temp_set:
                    total += abs(value - temp_set[i])
                if total < min_set:
                    min_set = total
            min_total += min_set
        out_str = str(min_total)
#        print min_total
    output.append("Case #" + str(case) + ": " + out_str )

write_output(output)


