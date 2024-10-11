def depth(arr, ans, idx, left, right):
    if idx > left:
        max_left = arr.index(max(arr[left : idx]), left, idx)
        ans[max_left] = ans[idx] + 1
        depth(arr, ans, max_left, left, idx-1)
    if idx < right:
        max_right = arr.index(max(arr[idx+1 : right+1]), idx+1, right+1)
        ans[max_right] = ans[idx] + 1
        depth(arr, ans, max_right, idx+1, right)

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = [0 for _ in range(n)]
    idx = arr.index(max(arr))
    depth(arr, ans, idx, 0, n-1)
    print(*ans)