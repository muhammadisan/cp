from collections import defaultdict

n, m = map(int, input().split())

isPrime = [True for _ in range(n+1)]
isPrime[0] = False
isPrime[1] = False
d = defaultdict(int)
d[1] = 0
num_primes = defaultdict(list)
for p in range(2, n+1):
    if isPrime[p]:
        d[p] = 0
        num_primes[p].append(p)
        for k in range(2, n):
            if k*p > n:
                break
            isPrime[k*p] = False
            num_primes[k*p].append(p)
            
for _ in range(m):
    op, num = input().split()
    num = int(num)
    if num == 1:
        if op == '-':
            if d[1] == 0:
                print("Already off")
            else:
                print("Success")
                d[1] = 0
        else:
            if d[1] == 0:
                print("Success")
                d[1] = 1
            else:
                print("Already on")
        continue

    if op == '-':
        isOff = True
        for p in num_primes[num]:
            if d[p] != num:
                print("Already off")
                break
            else:
                d[p] = 0
                isOff = False
        if not isOff:
            print("Success")
    else:
        divisors = []
        isConflict = False
        for p in num_primes[num]:
            if d[p] == num:
                isConflict = True
                print("Already on")
                break
            elif d[p] == 0:
                divisors.append(p)
            else:
                isConflict = True
                print("Conflict with", d[p])
                break
        if not isConflict:
            print("Success")
            for key in divisors:
                d[key] = num