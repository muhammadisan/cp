from collections import defaultdict

def min_ops(s):
  n = len(s)
  if n == 1:
    return 1
  
  if(n % 2 == 0):
    dict_even = defaultdict(int)
    dict_odd = defaultdict(int)
    for i in range(n):
      if i % 2 == 0:
        dict_even[s[i]] += 1
      else:
        dict_odd[s[i]] += 1
        
    max_even = 0
    max_odd = 0
    for key, val in dict_even.items():
      max_even = max(max_even, val)
    for key, val in dict_odd.items():
      max_odd = max(max_odd, val)
      
    return n - max_even - max_odd
  
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  pre_even = {c: [0 for _ in range(n)] for c in alphabet}
  post_even = {c: [0 for _ in range(n)] for c in alphabet}
  pre_odd = {c: [0 for _ in range(n)] for c in alphabet}
  post_odd = {c: [0 for _ in range(n)] for c in alphabet}
  
  for i in range(n):
    if i % 2 == 0:
      for c in alphabet:
        if c == s[i]:
          if i == 0:
            pre_even[c][0] += 1
          else:
            pre_even[c][i] = pre_even[c][i-2] + 1
        else:
          if i > 0:
            pre_even[c][i] = pre_even[c][i-2]
    else:
      for c in alphabet:
        if c == s[i]:
          if i == 1:
            pre_odd[c][1] += 1
          else:
            pre_odd[c][i] = pre_odd[c][i-2] + 1
        else:
          if i > 1:
            pre_odd[c][i] = pre_odd[c][i-2]
            
  for i in reversed(range(n)):
    if i % 2 == 0:
      for c in alphabet:
        if c == s[i]:
          if i == n-1:
            post_even[c][n-1] += 1
          else:
            post_even[c][i] = post_even[c][i+2] + 1
        else:
          if i < n-1:
            post_even[c][i] = post_even[c][i+2]
    else:
      for c in alphabet:
        if c == s[i]:
          if i == n-2:
            post_odd[c][n-2] += 1
          else:
            post_odd[c][i] = post_odd[c][i+2] + 1
        else:
          if i < n-2:
            post_odd[c][i] = post_odd[c][i+2]
              
  ans = float('inf')
  for i in range(n):
    if i % 2 == 0:
      max_even = 0
      max_odd = 0
      for c in alphabet:
        pre = pre_even[c][i-2] if i-2 >= 0 else 0
        post = post_odd[c][i+1] if i+1 < n else 0
        even = pre + post
        max_even = max(max_even, even)
      for c in alphabet:
        pre = pre_odd[c][i-1] if i-1 >= 0 else 0
        post = post_even[c][i+2] if i+2 < n else 0
        odd = pre + post
        max_odd = max(max_odd, odd)
        
      ans = min(ans, n - max_even - max_odd)
    else:
      max_even = 0
      max_odd = 0
      for c in alphabet:
        pre = pre_even[c][i-1] if i-1 >= 0 else 0
        post = post_odd[c][i+2] if i+2 < n else 0
        even = pre + post
        max_even = max(max_even, even)
      for c in alphabet:
        pre = pre_odd[c][i-2] if i-2 >= 0 else 0
        post = post_even[c][i+1] if i+1 < n else 0
        odd = pre + post
        max_odd = max(max_odd, odd)
      
      ans = min(ans, n - max_even - max_odd)
  
  return ans

t = int(input())
while t:
  n = int(input())
  s = input()
  print(min_ops(s))
  t -= 1