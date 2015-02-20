def solution(A):
    # write your code in Python 2.7
    max_ending = max_slice = 0        
    for item in A:
        max_ending = max(0, max_ending + item)
        max_slice = max(max_ending, max_slice)
    return max_slice

def solution(A):
    # write your code in Python 2.7
    max_ending = max_slice = 0 
    min_neg = -float("Inf")
    found_pos = False
    for item in A:
        max_ending = max(0, max_ending + item)
        max_slice = max(max_ending, max_slice)
        if max_slice > 0:
            found_pos = True
        if item < 0 and item > min_neg:
            min_neg = item
    if found_pos:
        return max_slice
    else:
        if min_neg == -float("Inf"):
            return 0
        else:
            return min_neg

