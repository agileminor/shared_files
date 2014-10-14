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

for word in lang_words:
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
    word_list = [[[],start_node]]
    current_node = start_node
    # switch to using queue instead of for looks
    # while queue is not empty, pop item off queue, add letter add on to back of queue
    # complex because of multiple letters, similar to jumble
    for item in test_word:
        for word in word_list:
            print "word", word, "in", word_list, item, "in", test_word
            letter_added = False
            for letter in item:
                print "letter is ", letter
                if letter in word[1].children:
                    word[0].append(letter)
                    word[1] = word[1].children[letter]
                    letter_added = True
            if not(letter_added):
                print "removing", word
                word_list.remove(word)
    output.append("Case #" + str(case) + ": %i" % len(word_list))
    case += 1
write_output(output)


