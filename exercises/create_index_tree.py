#!/usr/bin/env python

from collections import deque


class Node(object):
    """ Simple node for a tree structure. Note that value must be hashable to use this class.
        Node is customized to add index and cum string value"""
    def __init__(self, parent, value, count):
        self.parent = parent
        self.value = value
        self.children = {}
        if parent is not None:
            self.parent.children[self.value] = self
            self.cum_value = self.parent.cum_value + self.value
            self.index = count
        else:
            self.cum_value = ""
            self.index = 0


def append_letters(letter_list, parrent_node, queue, count):
    """Modifies a queue to add new children.

    Args:
        letter_list: string of allowable characters for children
        parent_node: node to add to children to
        queue: queue to keep track of nodes for next level of tree
        count: index of current word. current word = accumulation of values as you pass down the tree

    Returns:
        An integer representing the current count for indexing
    """

    for letter in letter_list:
        count = count + 1
        queue.append(Node(parrent_node, letter, count))
        #print queue[-1].cum_value, queue[-1].index # print statement useful to get all index values
    return count

def create_index_tree(letter_list):
    """Creates a tree where each node has a letter value, a cumulative value and an index

    Args:
        letter_list: string containing list of characters to be used in the word index tree

    Returns:
        The first node in the tree
    """
    count = 0
    start_node = Node(None,0,count)
    depth = 1
    node_queue = deque()
    count = append_letters(letter_list,start_node,node_queue, count)
    while depth < 5:
        next_level_queue = deque()
        depth += 1
        while node_queue:
            current_node = node_queue.popleft()
            current_letters = letter_list[letter_list.index(current_node.value)+1:]
            count = append_letters(current_letters, current_node, next_level_queue, count)
        node_queue = next_level_queue
    return start_node


def return_index(current_node, word):
    """Returns word and associated word index.

    Checks for valid words, then traverses tree until it finds the input word.

    Args:
        current_node: first node of tree
        word: word to search for

    Returns:
        A tuple of the word found, which should match the input word and an integer representing the associated index value.
    """
    if len(word) > 5:
        return (word,0)
    for letter in word:
        if letter in current_node.children:
            current_node = current_node.children[letter]
        else:
            return (word,0)
    return current_node.cum_value, current_node.index


def calc_index(word):
    """Returns just word index

    Simple wrapper function to return just index, if desired

    Args:
        word: word to be searched for

    Returns:
        An integer associated with input word.
    """
    return return_index(start_node, word)[1]

# set up input letters and index tree
letter_list = "abcdefghijklmnopqrstuvwxyz"
start_node = create_index_tree(letter_list)

# some sample outputs for checks
print return_index(start_node, "abc") # should return 352
print return_index(start_node, "cat") # should return 0 since input is not valid
print return_index(start_node, "vwxyz") # should return 83681
print return_index(start_node, "abcdef") # should return 0 since input is not valid

print calc_index("abc") # should return 352

