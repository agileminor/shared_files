def solution(A):
    # write your code in Python 2.7
    #print "A=",A
    N = len(A)
    peak_list = []
    for index in range(1,len(A)-1):
        if A[index - 1] < A[index] and A[index + 1] < A[index]:
            peak_list.append(index)
    if not peak_list:
        return 0
    #print peak_list
    factor_list = []
    for item in range(1,int(N ** .5)+1):
        if N % item == 0:
            factor_list.append(item)
            if N/item != item:
                factor_list.append(N/item)
    #print factor_list
    working_factor_count = 0
    working_factor_list = []
    peak_len = len(peak_list)
    max_blocks = 0
    for item in factor_list:
        #print "checking", item
        if N/item <= max_blocks:
            break
        index = 0
        for mult in range(1,N/item + 1):
            found_peak = False
            max_value = mult * item - 1
            min_value = (mult - 1) * item
            while index < len(peak_list):
                if peak_list[index] <= max_value and peak_list[index] >= min_value:
                    #print item, mult, max_value,min_value, peak_list[index]
                    found_peak = True
                    break
                index += 1
            if not found_peak:
                break
        else:
            #print "found ", item
            max_blocks = N/item

            #working_factor_list.append(item)
    return max_blocks
    
def solution2(A):
    import random
    random.seed()
    rand_A = [random.randint(0,6) for a in range(12)]
    print rand_A
    print solution_to_test(rand_A)
    
    return solution_to_test(A)

