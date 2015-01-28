def solution(A, B, K):
    # write your code in Python 2.7
    x = [1 for a in range(A,B+1) if a % K == 0]
    print sum(x)
    if B < K: 
        if A == 0:
            return 1
        else:
            return 0
    if A % K == 0:
        return (B - A ) / K + 1
    else:
        return (B - A + A % K) / K

