def sieve_old(max):
    primes = range(2,max+1)
    index = 0
    current = 2
    removed = {}
    while current < max:
        print "current = ", current
        inner_index = current
        while current*inner_index <= max:
            print "inner = ", inner_index
            if current * inner_index not in removed:
                removed[current * inner_index] = 1
                primes.remove(current*inner_index)
            inner_index += 1
        index += 1
        if index == len(primes):
            break
        current = primes[index]
    return primes
def sieve(max):
    primes = range(2,max+1)
    current = 2
    index = 0
    while current < max:
#        print current
        prime1 = primes[:index]
        prime2 = [a for a in primes[index:] if (a == current or a % current != 0)]
        primes = prime1 + prime2
        index += 1
        if index == len(primes):
            break
        current = primes[index]

    return primes

def sieve3(max): # from stack overflow
    primes = []
    valid = [True] * (max + 1)
    for value in range(2, max + 1):
        if valid[value]:
            primes.append(value)
            for i in range(value * value, max + 1, value):
                valid[i] = False
    return primes
