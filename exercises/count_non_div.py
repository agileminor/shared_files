def divisors(i, A_set,A_dict):
    #print "i = ", i
    list_len = 0
    for a in range(1, int(i ** .5) + 1):
        #print "a = ", a
        if i %a == 0:
            #print "found divisor"
            if a in A_set:
                #print "found in list"
                list_len += A_dict[a]
            if i / a != a:
                #print "found 2nd divisor"
                if i / a in A_set:
                    list_len += A_dict[i / a]
    #print "list_len = ", list_len
    return list_len
        
        
def solution(A):
    # write your code in Python 2.7
    A_set = set(A)
    A_dict = {}
    div_dict = {}
    A_len = len(A)
    for item in A:
        if item in A_dict:
            A_dict[item] += 1
        else:
            A_dict[item] = 1
    out = []
    for item in A:
        if item in div_dict:
            difference_len = div_dict[item]
        else:
            difference_len = divisors(item,A_set, A_dict)
            div_dict[item] = difference_len
        count = 0
        #for i in difference_set:
        #    count += A_dict[i]
        out.append(A_len - difference_len)
    return out

