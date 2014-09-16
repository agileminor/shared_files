# you can use print for debugging purposes, e.g.
# print "this is a debug message"
import math


def test_valid(N, point):
    if math.sqrt(pow(point[0],2) + pow(point[1],2)) <= N:
        #print "found valid"
        return True
    else:
        return False


def solution(N):
    # write your code in Python 2.7
    if N < 0 or N > 20000:
        print "N outside valid input range"
        return -1
    valid_frontier = []
    valid_count = N * 4 + 1 # base case of vertical axis
    # add special case for point on axis later
    current_point = [N-1,1]
    move_vertical = True
    while current_point[0] != 0:
        #print current_point
        if test_valid(N, current_point):
            #valid_frontier.append(current_point)
            valid_count += current_point[0] * 4 # by symmetry about origin
            if not move_vertical:
                move_vertical = True
        else:
            if move_vertical:
                move_vertical = False
        if move_vertical:
            #print "found vertical"
            next_point = [current_point[0], current_point[1] + 1]
        else:
            next_point = [current_point[0]-1, current_point[1]]
        if valid_count > 1000000000:
            return -1
        current_point = next_point
    return valid_count

