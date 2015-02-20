def solution(A):
    # write your code in Python 2.7
    N = len(A)
    peak_list = []
    for index in range(1,len(A)-1):
        if A[index - 1] < A[index] and A[index + 1] < A[index]:
            peak_list.append(index)
    if not peak_list:
        return 0
    #print peak_list
    max_flags = len(peak_list)
    if max_flags == 2:
        if peak_list[1] - peak_list[0] >= 2:
            return 2
        else:
            return 1
    upper = max_flags 
    lower = 1  
    difference = upper - lower
    current = -((-(upper-0))/2)
    while difference != 0:
        #print current
        
        flags_available = max_flags
        flag_count = max_flags
        back_index = 0
        front_index = 1
        while front_index < max_flags:
            #print "counting flags"
            while peak_list[front_index] - peak_list[back_index] < current:
                front_index += 1
                flag_count -= 1
                if flag_count < current or front_index == max_flags:
                    break
            else:
                back_index = front_index
                front_index += 1
            if flag_count < current:
                difference = upper - lower
                if current == upper:
                    difference = 0
                    return current -1
                else:
                    upper = current
                    #print current, "failed", upper, lower, difference
                
                    current = current - (-((-(upper-lower))/2))
                break
        else:
            #print "done counting"
            if flag_count >= current:
                difference = upper - lower
                if lower == current:
                    difference = 0
                    return current
                else:
                    lower = current
                    #print current, "worked", upper, lower, difference
                    current = current + (-((-(upper-lower))/2))
                
    else:
        return current
                
    return 1
                
                    
def solution2(A):
    import random
    random.seed()
    rand_A = [random.randint(0,8) for i in range(10)]
    print rand_A
    x = solution_to_test(rand_A)
    print "rand = ", x
    
    return solution_to_test(A)
