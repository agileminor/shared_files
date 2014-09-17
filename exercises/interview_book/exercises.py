#!/usr/bin/env python

def check_unique(word):
    # Exercise 1.1
    letter_hash = {}
    for letter in word:
        if letter not in letter_hash:
            letter_hash[letter] = 1
        else:
            return letter + " is not unique in " + word
    return "No non-unique letters in " + word

def generate_letter_array(word):
    letter_hash = {}
    for letter in word:
        if letter not in letter_hash:
            letter_hash[letter] = 1
        else:
            letter_hash[letter] += 1
    return letter_hash


def compare_strings(first, second):
    # Exercise 1.3
    if len(first) != len(second):
        return first + " is not a variant of " + second
    if generate_letter_array(first) == generate_letter_array(second):
        return first + " is a variant of " + second
    else:
        return first + " is not a variant of " + second

def replace_blank(word):
    # Exercise 1.4
    word_list = []
    for letter in word:
        if letter == " ":
            word_list.append("%20")
        else:
            word_list.append(letter)
    return "".join(word_list)


def compress_string(word):
    # Exercise 1.5
    count = 0
    last_letter = word[0] 
    new_word = []
    for letter in word:
        if letter == last_letter:
            count = count + 1
        else:
            new_word.append(last_letter)
            new_word.append(str(count))
            count = 1
            last_letter = letter
    new_word.append(last_letter)
    new_word.append(str(count))

    if len(new_word) >= len(word):
        return word
    else:
        return "".join(new_word)

class NodeSingle(object):
    def __init__(self,data,next_node=None):
        self.data = data
        self.next_node = next_node

def delete_dup_node(start_node):
    value_list = {}
    current_node = start_node
    while current_node.next_node != None:
        temp_node = current_node.next_node
        if current_node.value in value_list:
            previous_node.next_node = temp_node
            del(current_node)
        else:
            value_list[current_node.value] = 1
            previous_node = current_node
        current_node = temp_node

def return_kth_from_end(start_node,k):
    count = 0
    current_node = start_node
    return_node = start_node
    while current_node.next_node != None:
        current_node = current_node.next_node
        if count >= k:
            return_node = return_node.next_node
        count += 1
    return return_node.value
