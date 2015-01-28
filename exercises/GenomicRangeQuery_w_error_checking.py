def solution_slow(S, P, Q):
    print "running slow"
    check_dict = {"A":1, "C":2, "G":3, "T":4}
    M = []
    for (index, item) in enumerate(P):
        check_range = range(item,Q[index]+1)
        min_check = 5
        for check in check_range:
            if check_dict[S[check]] < min_check:
                min_check = check_dict[S[check]]
        M.append(min_check)
    return M


def solution_real(S, P, Q, test = False):
    if test:
        print "running tests"
    # write your code in Python 2.7
    val_dict = {"A":1, "C":2, "G":3, "T":4}
    
    M = []
    for (index, item) in enumerate(P):
        check_set = set(S[item:Q[index]+1])
        if "A" in check_set:
            M.append(1)
        elif "C" in check_set:
            M.append(2)
        elif "G" in check_set:
            M.append(3)
        else:
            M.append(4)
    return M

    if test:
        solution_check = solution_slow(S, P, Q)        
        if solution_check != M:
            print solution_check, M
    return M

def solution(S, P, Q): # still N * M, need speedup
    test = True

    if test:
        import random
        random.seed()
        reverse_dict = {1:"A",2:"C",3:"G",4:"T"}
        N = random.randint(1,100000)
        M = random.randint(1,50000)
        int_list = [reverse_dict[random.randint(1,4)] for a in range(N)]
        S_rand = "".join(int_list)
        P_rand = [random.randint(0,N-1) for a in range(M)]
        
        Q_rand = [random.randint(a, N-1) for a in P_rand]
        result = solution_real(S_rand, P_rand, Q_rand, True) 
    print "running real"

    return solution_real(S, P, Q)

