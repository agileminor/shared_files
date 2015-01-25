def solution(A):
# write your code in Python 2.7
    attract_set = set(A)
    #print attract_set
    left_set = set([])
    left_index = 0
    for item in A:
        if left_set.issuperset(attract_set):
            break
        left_set.update([item])
        left_index += 1
    right_index = len(A)
    right_set = set([])
    while not right_set.issuperset(attract_set):
        right_index -= 1
        right_set.update([A[right_index]])

    return max(0,right_index - left_index + 1)


def solution_fast(A):
# write your code in Python 2.7
    attract_set = set(A)
    attract_len = len(attract_set)
    #print attract_set
    left_set = set([])
    left_index = 0
    for item in A:
        if len(left_set) == attract_len:
            break
        left_set.update([item])
        left_index += 1
    right_index = len(A)
    right_set = set([])
    while len(right_set) != attract_len:
        right_index -= 1
        right_set.update([A[right_index]])

    return max(0,right_index - left_index + 1)
