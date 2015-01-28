def solution_slow(A):
    # write your code in Python 2.7
    prefix = []
    start = 0 
    for (index,item) in enumerate(A):
        start += item
        prefix.append(start)
    counter = 0
    min_average = float("Inf")
    found_min = len(A)
    for P in range(counter, len(A)):
        for Q in range(P+1, len(A)):
            if P == 0:
                temp_sum = float(prefix[Q])
                temp_average = temp_sum/(Q-P+1)
            else:    
                temp_sum = float(prefix[Q] - prefix[P-1])
                temp_average = temp_sum/(Q-P+1)
            if temp_average < min_average:
                min_average = temp_average
                found_min = P
            
    return found_min

def solution(A):
    min_average = float("Inf")
    min_index = 0
    for P in range(len(A)-2):
        min2 = float(A[P] + A[P+1])/2
        min3 = float(A[P] + A[P+1] + A[P+2])/3
        if min2 < min_average:
            min_average = min2
            min_index = P
        if min3 < min_average:
            min_average = min3
            min_index = P
    if float(A[-2] + A[-1])/2 < min_average:
        min_index = len(A) - 2
    return min_index
        

