#!/usr/bin/python
import time


class Node(object):
    """ Simple node for a tree structure. Note that value must be hashable to use this class."""
    def __init__(self, parent, value):
        self.parent = parent
        self.value = value
        self.children = {}
        if parent is not None:
            self.parent.children[self.value] = self


def load_dict(filename):
    """ reads in file of words, returns a python dictionary for quick searching and a tree showing valid letter
    sequences."""
    dict_handle = open(filename, 'r')
    word_dict = {}
    root = Node(None, '')
    for word in dict_handle:
        current_node = root
        word = word.strip().lower()
        if word not in word_dict and len(word) > 1:
            word_dict[word] = 1
        for letter in word:
            if letter in current_node.children:
                next_node = current_node.children[letter]
            else:
                next_node = Node(current_node, letter)
            current_node = next_node
    return word_dict, root
        

def do_boggle(board, word_dict, letter_tree_root):
    """ reads in a board (2d nXn array of letters, dictionary and the root node of letter tree. 
        Returns a list of valid words constructed from board."""
    initial_moves = [(a, b) for a in [-1, 0, 1] for b in [-1, 0, 1]]
    words = []
    size = len(board)
    # iterate over all possible starting locations
    for row_index in range(size):
        for column_index in range(size):
            visited_spaces = []
            current_word = []
            recurse_board(board, visited_spaces, current_word, words, [row_index, column_index], word_dict, initial_moves, letter_tree_root)
    return words


def scrub_locations(new_locations, visited_spaces, n):
    """ takes a list of locations and valid spaces and returns a list of realistic moves."""
    scrubbed_locations = []
    for location in new_locations:
        if location in visited_spaces:
            pass
        elif location[0] < 0 or location[1] < 0 or location[0] == n or location[1] == n:
            pass
        else:
            scrubbed_locations.append(location)
    return scrubbed_locations


def is_word(word, word_dict):
    """ Checks if target string is in given dictionary."""
    if word in word_dict:
        return True
    else:
        return False


def recurse_board(board, visited_spaces, current_word, words, location, word_dict, initial_moves, current_tree_node):
    """ for a given board, list of visited spaces, starting string, and location, continues recursion if there
    are valid new locations, returns None if letter sequence can not lead to a word, returns 1 when no more new
    locations."""
    new_locations = []
    visited_spaces.append(location)
    current_letter = board[location[0]][location[1]]
#    print current_letter
#    print current_tree_node.children

### check for valid letter sequences, end recursion of no longer valid
    if current_letter not in current_tree_node.children:  # check
        return None
    current_tree_node = current_tree_node.children[current_letter]
    current_word.append(current_letter)
    current_word_string = "".join(current_word)
    if is_word(current_word_string, word_dict):
        words.append(current_word_string)
    #print "current_word = ", current_word_string
    #print "words = ", words
    for move in initial_moves:
        new_location = [move[0] + location[0], move[1] + location[1]]
        new_locations.append(new_location)
    new_locations = scrub_locations(new_locations, visited_spaces, len(board))
    #print "new_locations = ", new_locations
    #print "visited_spaces = ", visited_spaces
    for new_location in new_locations:
        recurse_value = recurse_board(board, visited_spaces, current_word, words, new_location, word_dict, initial_moves, current_tree_node)
### remove values added to reference passed lists in last level of recursion. If recursion encountered invalid letter sequence, only remove visited space, otherwise remove space + letter
        if recurse_value:
            current_word.pop() 
        visited_spaces.pop() 
        #print "returned visited = ", visited_spaces
        #print "returned word = ", current_word
    return 1

### program execution start
### set up dictionary and tree
start_time = time.time()
word_dict, letter_tree_root = load_dict('/usr/share/dict/words')
#print word_dict
#print letter_tree_root.children
print("load dict time = %2.2f" % (time.time() - start_time))

### create board

#board = [['m','a','i','l'],['a','i','r','o'],['t','w','b','s'],['h','s','t','u']]
board = ['mail', 'airo', 'twbs', 'hstu']
start_time = time.time()

### create word list from board
words = do_boggle(board, word_dict, letter_tree_root)
    
print("do boggle time = %2.2f" % (time.time() - start_time))
print words
