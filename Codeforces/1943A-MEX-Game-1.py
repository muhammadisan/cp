t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = [0]*n
    for el in a:
        count[el] += 1
    
    ans = n
    flag1 = False
    for i in range(n):
        if count[i] == 0:
            ans = i
            break
        elif count[i] == 1:
            if not flag1:
                ans = i+1
                flag1 = True
            else:
                ans = i
                break
    print(ans)