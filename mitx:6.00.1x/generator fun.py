def genPrimes():
    l = []
    i = 2
    while True:
        flag = 1
        for p in l:
            if (i%p) == 0:
                flag = 0
                break
        if flag == 1:
            l.append(i)
            yield i
        i+= 1


"""
usage:
a = genPrimes()
a.next()

or

for i in range(20) #generates 20 consecutive primes
    a.next()
