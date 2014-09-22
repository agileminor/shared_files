#!/usr/bin/env python

max_seg = {1:"z",2:"yz",3:"xyz",4:"wxyz",5:"vwxyz"}
word_dict = {}

def return_value(letter):
    return ord(letter) - 96


def return_char(value):
    return chr(value + 96)


def check_min(word):
    last_value = return_value(word[0])
    for i in range(1,len(word)):
        current_value = return_value(word[i])
        if (current_value - last_value) != 1:
            return False
        last_value = current_value
    return True


def return_min(word):
    new_word = [word[0]]
    for i in range(1,len(word)):
        new_value = return_value(word[0]) + i
        new_word.append(return_char(new_value))
    return "".join(new_word)

def calc_prev_word(word):
    new_word = []
    for letter in word:
        new_letter = return_char(return_value(letter) - 1)
        new_word.append(new_letter)
    return "".join(new_word)


def calc_min_index(word):
    if word in word_dict:
        return word_dict[word]
    if len(word) == 1:
        return return_value(word)
    if word[0] == "a":
        return calc_index(max_seg[len(word)-1]) + 1
    else:
        prev_word = calc_prev_word(word)
        term1 =  calc_index(prev_word)
        term2 =  calc_index(max_seg[len(word)-1]) 
        term3 =  calc_index(calc_prev_word(prev_word[1:]))
        return term1 + term2 - term3
#        return calc_index(prev_word) + calc_index(max_seg[len(word)-1]) - calc_prev_word(prev_word[1:])


def calc_non_min_index(word):
    if len(word) == 1:
        return return_value(word)
    if word in word_dict:
        return word_dict[word]
    new_min = return_min(word)
    term1 =  calc_index(new_min)
    term2 =  calc_index(word[1:]) 
    term3 =  calc_index(new_min[1:])
    word_dict[word] = term1 + term2 - term3
    return term1 + term2 - term3
#    return calc_index(new_min) + calc_index(word[1:]) - calc_index(new_min[1:])


def calc_index(word):
    if word in word_dict:
        return word_dict[word]
    if len(word) == 1:
        return return_value(word)
    if check_min(word):
        return calc_min_index(word)
    else:
        return calc_non_min_index(word)

print calc_index("abc") # correct
print calc_index("acd") # correct
print calc_index("ayz") # correct
print calc_index("yz") # correct
print calc_index("bcd") #incorrect - should be 652
