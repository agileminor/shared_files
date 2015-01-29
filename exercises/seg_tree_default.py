#!/usr/bin/env python
import math
class SegTreeMin(object):
    # segmented tree to give min of interval i,j
    # value_array = length N input array
    # tree_array length = 2 ^ (math.ceil(math.log(N,2)+1)
    # tree_array gives position of min for matching interval
    # for tree_array[i] tree_array[2 * i +1] = left child, tree_array[2 * i + 2] = right node
    # if interval for parent is [i,j], left child is interval [i,(i+j)/2] and right child is interval [(i+j)/2+1,j]
    # to construct, call with current = 0, lower = 0, upper = N - 1


    def __init__(self,value_array):
        self.value_array = value_array
        self.N = len(value_array)
        self.tree_array = [-1] * ( 2 ** int(math.ceil(math.log(self.N, 2)+1))) 
        self.create_tree(0, 0, self.N - 1, self.tree_array, self.value_array,self.N)


    def create_tree(self, current, lower, upper, tree_array, value_array, N):
            # populate positions in tree
        if lower == upper: # root nodes
#            tree_array[current] = value_array[lower]
            tree_array[current] = lower
        else: # create left/right sub trees
            self.create_tree(2 * current + 1, lower, (lower + upper) / 2, tree_array, value_array, N)
            self.create_tree(2 * current + 2, (lower + upper) /2 + 1,upper, tree_array, value_array, N)
                # propogate min positions upward
            if value_array[tree_array[2 * current+1]] <= value_array[tree_array[2 * current + 2]]:
                tree_array[current] = tree_array[2* current + 1]
            else:
                tree_array[current] = tree_array[2 * current + 2]

    
    def query_position(self, current, lower, upper, tree_array, value_array, N, i, j):
        # returns position of min value in interval i, j
        if (i > upper or j < lower):
            return - 1
        if (lower >= i and upper <= j):
            return tree_array[current]
        left = self.query_position(2 * current + 1, lower, (lower+upper)/2,tree_array, value_array, self.N, i, j)
        right = self.query_position(2 * current + 2, (lower+upper)/2 + 1, upper, tree_array, value_array, self.N, i, j)
        if left == -1:
            return right
        if right == -1:
            return left
        if value_array[left] <= value_array[right]:
            return left
        else:
            return right


    def query_min(self, i,j):
        #returns actual min value in interval i, j
        return self.value_array[self.query_position(0,0,self.N - 1,self.tree_array, self.value_array, self.N, i, j)]
