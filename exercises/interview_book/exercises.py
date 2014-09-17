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
            count += 1
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
    """Node for a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


def delete_dup_node(start_node):
    value_list = {}
    current_node = start_node
    while current_node.next_node:
        temp_node = current_node.next_node
        if current_node.value in value_list:
            previous_node.next_node = temp_node
            del current_node
        else:
            value_list[current_node.value] = 1
            previous_node = current_node
        current_node = temp_node


def return_kth_from_end(start_node, k):
    count = 0
    current_node = start_node
    return_node = start_node
    while current_node.next_node != None:
        current_node = current_node.next_node
        if count >= k:
            return_node = return_node.next_node
        count += 1
    return return_node.value


def add_lists(list1,list2):
    """takes two numbers stored in linked lists in single digits, reverse order, adds them and returns the result in
        a third linked list."""
    result_list = NodeSingle(0)
    current_list1 = list1
    current_list2 = list2
    current_result = result_list
    done_list1 = False
    done_list2 = False
    carry = 0
    while (done_list1 == False or done_list2 == False):
        if done_list1 == True:
            value1 = 0
        else:
            value1 = current_list1.data
        if done_list2 == True:
            value2 = 0
        else:
            value2 = current_list1.data
        (carry, new_value) = divmod(value1 + value2 + carry, 10)
        current_result.data = new_value
        current_result.next_node = NodeSingle(0)
        current_result = current_result.next_node
        if current_list1.next_node:
            current_list1 = current_list1.next_node
        else:
            done_list1 = True
        if current_list2.next_node:
            current_list2 = current_list2.next_node
        else:
            done_list2 = True
    if carry == 1:
        current_result.data = carry
    else:
        del current_result
    return result_list

def find_loop(start_node):
    """Find if a linked list has a loop."""
    slow_node = start_node
    fast_node = start_node
    while (slow_node.next_node and fast_node.next_node.next_node):
        slow_node = slow_node.next_node
        fast_node = fast_node.next_node.next_node
        if slow_node == fast_node:
            return True
    return False


def find_loop_start(start_node):
    """Find first node of loop in list."""
    slow_node = start_node
    fast_node = start_node
    in_loop = False
    while (1):
        slow_node = slow_node.next_node
        fast_node = fast_node.next_node.next_node
        if slow_node == fast_node:
            if not in_loop:
                in_loop = True
                slow_node = start_node
            else:
                return slow_node
        


