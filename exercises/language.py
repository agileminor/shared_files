#!/usr/bin/env python

import sys
from code_jam_io import read_input
from code_jam_io import write_output

class Node(object):
    def __init__(self, value):
        self.value = value
        self.children = {}
start_node = Node(0)
num_cases, contents = read_input()
L = int(contents[0][0])
D = int(contents[0][1])
N = int(contents[0][2])
print contents
print L, D, N
lang_words = [word[0] for word in contents[1:D+1]]
print lang_words
test_words = [word[0] for word in contents[D+1:]]
print test_words
word_dict = {}

for word in lang_words:
    word_dict[word] = 1
    current_node = start_node
    for letter in word:
        if letter in current_node.children:
            current_node = current_node.children[letter]
        else:
            current_node.children[letter] = Node(letter)
            current_node = current_node.children[letter]

output = []
eval_words = []
for word in test_words:
    temp_word = []
    in_temp = False
    for letter in word:
        if letter == "(":
            temp = []
            in_temp = True
        elif letter == ")":
            temp_word.append("".join(temp))
            in_temp = False
        elif in_temp:
            temp.append(letter)
        else:
            temp_word.append(letter)
    eval_words.append(temp_word)
print eval_words
case = 1
for test_word in eval_words:
    score = 0
    word_list = [[[],start_node]]
    queue = [[[],start_node]]
    # switch to using queue instead of for looks
    # while queue is not empty, pop item off queue, add letter add on to back of queue
    # complex because of multiple letters, similar to jumble
    while queue != []:
        current_item = queue[0]
        queue = queue[1:]
        for item in test_word:
            for letter in item:
                if letter in current_item[1].children:
                    new_word = current_item[0][:]
                    new_word.append(letter)
                    if "".join(new_word) in word_dict:
                        score += 1
                    else:
                        queue.append([new_word,current_item[1].children[letter]])
    output.append("Case #" + str(case) + ": %i" % score )
    case += 1
write_output(output)


