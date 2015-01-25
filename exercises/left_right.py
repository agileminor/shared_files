#!/usr/bin/env python
import random

def solution(S):
        # write your code in Python 2.7
    initial = int(S)
    if len(S) % 2 == 1:
        new = ["1"] + ["0"] * (len(S)/2) # original incorrect - new = ["1"] * (len(S) + 1)
        new = new + new
        new = "".join(new)
        return new
    else:
        left = int(S[:len(S)/2])
        right = int(S[len(S)/2:])
        #print left
        #print right
        if right < left:
            return str(left) + str(left)
        else:
            left += 1
            return str(left) + str(left)

def check_valid(S):
    if len(S) % 2 == 1:
        return False
    else:
        left = int(S[:len(S)/2])
        right = int(S[len(S)/2:])
        if left == right:
            return True
        else:
            return False

def gen_S():
    return str(random.randint(1,1000000))

def solution_slow(S):
    number = int(S)
    number += 1
    while not check_valid(str(number)):
            number += 1
    return str(number)
for a in range(1000):
    test_value = gen_S()
    fast = solution(test_value)
    slow = solution_slow(test_value)
    if slow != fast:
        print "solution for", test_value, fast, "vs", slow, fast == slow
