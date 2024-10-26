t = int(input())
for _ in range(t):
    n = int(input())
    x = 0
    sakurako_turn = True
    i = 1
    while -n <= x and x <= n:
        if sakurako_turn:
            x -= 2*i - 1
            sakurako_turn = False
        else:
            x += 2*i - 1
            sakurako_turn = True
        i += 1