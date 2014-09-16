from itertools import combinations

def check_valid(points,A):
    p = points[0]
    q = points[1]
    r = points[2]
    if (A[p] + A[q] > A[r] and
        A[q] + A[r] > A[p] and
        A[r] + A[p] > A[q]):
            return A[p] + A[q] + A[r]
    else:
        return None

def solution(A):
    current_min = float("inf")
    possible_triangles = combinations(range(len(A)),3)
    for triangle in possible_triangles:
        valid_test = check_valid(triangle, A)
        #print triangle, valid_test
        if valid_test:
            if valid_test < current_min:
                current_min = valid_test
    if current_min == float("inf"):
        return -1
    else:
        return current_min
def solution_fast(A):
    A.sort()
    n = len(A)
    for i in range(n-2):
        for j in range(i+1,n-1):
            if A[i] + A[j] > A[j+1]:
                return A[i] + A[j] + A[j+1]
    return -1
A = [1,1,1,1,1]
print solution_fast(A)

