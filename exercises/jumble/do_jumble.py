#!/usr/bin/python
import time
import sys

class Node(object):
    """ Simple node for a tree structure. Note that value must be hashable to use this class."""
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.children = {}
        if parent is not None:
            self.parent.children[self.value] = self


def timer(func):
    def time_func(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        print func.__name__, " takes %2.2f seconds"%(time.time()-start_time)
        return ret
    return time_func

@timer
def load_dict(filename):
    """ reads in file of words, returns a python dictionary of sorted words and associated valid words. Ignores 1 length words
        Also returns the root of a tree made up of the letter sequences of the sorted words. Used to prune later searches.""" 
    dict_handle = open(filename, 'r')
    word_dict = {}
    root = Node(None, '')
    for word in dict_handle:
        current_node = root
        word = word.strip().lower()
        sorted_word = "".join(sorted(word))
        if sorted_word not in word_dict and len(word) > 1:
            word_dict[sorted_word] = [word]
            for letter in sorted_word:
                if letter in current_node.children:
                    next_node = current_node.children[letter]
                else:
                    next_node = Node(current_node, letter)
                current_node = next_node
        elif len(word) > 1:
            if word not in word_dict[sorted_word]:
                word_dict[sorted_word].append(word)
    return word_dict, root


def do_comb(input,output, k, current_tree_node):
    """ Takes 2 input lists. Creates combination without replacement for n choose k of input list and adds it to output list."""
    n = len(input)
    if n == k:
        output.append(input)
    elif k == 1:
        for item in input:
            output.append(item)
    else:
        start = input[0]# check if b in children, if not, skip down to do_comb[i:],output,k]
        if start in current_tree_node.children:
            current_tree_node = current_tree_node.children[start]
            temp_output = []
            do_comb(input[1:], temp_output, k-1, current_tree_node)
            output += [start + item for item in temp_output]
#        for item in temp_output:
#            output.append(start + item)
        do_comb(input[1:], output, k, current_tree_node)


@timer
def jumble(input, word_dict, root):
    """ Takes as inputs a non-zero length string and a dictionary with key = sorted word, value = list of matching words. Returns list of possible words to make from input.
    Ignores 1 letter words"""
    ### check for valid inputs
    if not isinstance(input, basestring):
        print "Input is not a string. Exitting"
        sys.exit()
    sorted_input = "".join(sorted(input))
    input_length = len(sorted_input)
    if input_length == 0:
        print "Input string must be non zero length"
        sys.exit()
    ### create possible combinations of input string using do_comb function
    sorted_combos = []
    for i in range(2, input_length+1): # indexed from 2 to not include 1 length words
        do_comb(sorted_input, sorted_combos, i, root)
    sorted_combos = list(set(sorted_combos))
    word_list = []
    ### concatenate valid words based on input word list
    for trial_string in sorted_combos:
        if trial_string in word_dict:
            word_list += word_dict[trial_string]
#            print "adding", word_dict[trial_string]," for",trial_string
    return word_list

###
#Below code loads in a word list then does a jumble on a sample word

if __name__ == '__main__':
#    word_list = load_dict('/usr/share/dict/words')
    word_list, tree_root = load_dict('/usr/share/dict/words')
    sample_word = "stranger"
    words = jumble(sample_word,word_list, tree_root)
    print words
            

